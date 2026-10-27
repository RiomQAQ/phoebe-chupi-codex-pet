"""Exercise real release boundaries without replacing the shipped artwork."""
from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_artwork import audit, STANDARD_SHA256
from restore_outlines import HISTORICAL_WEBP, load, sha


class ApprovedArtworkRegression(unittest.TestCase):
    LOOK_PIXEL = (80, 9 * 208 + 120)

    @classmethod
    def setUpClass(cls):
        cls.fixture_directory = tempfile.TemporaryDirectory()
        fixture = Path(cls.fixture_directory.name)
        cls.reviewed_source = fixture / "reviewed.png"
        cls.reviewed_runtime = fixture / "reviewed.webp"
        artwork = load(ROOT / "art/releases/v1.0.1/spritesheet.png")
        r, g, b, alpha = artwork.getpixel(cls.LOOK_PIXEL)
        # A reviewed v1.0.2 look change may intentionally change RGB and alpha.
        artwork.putpixel(cls.LOOK_PIXEL, ((r + 1) % 256, g, b, alpha - 1))
        artwork.save(cls.reviewed_source)
        artwork.save(cls.reviewed_runtime, format="WEBP", lossless=True, exact=True, method=0)

    @classmethod
    def tearDownClass(cls):
        cls.fixture_directory.cleanup()

    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "art/approved/v1.0.2/spritesheet.png"
        self.standard = self.root / "art/releases/v1.0.1/spritesheet.png"
        self.runtime = self.root / "pets/phoebe-chupi/spritesheet.webp"
        self.manifest_path = self.root / "art/approved-runtime.json"
        for path in (self.source, self.standard, self.runtime):
            path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(self.reviewed_source, self.source)
        shutil.copy2(self.reviewed_runtime, self.runtime)
        shutil.copy2(ROOT / "art/releases/v1.0.1/spritesheet.png", self.standard)
        (self.root / "VERSION").write_text("v1.0.2\n", encoding="utf-8")
        self.manifest = {
            "version": "v1.0.2",
            "source": {"path": self.source.relative_to(self.root).as_posix(), "sha256": sha(self.source)},
            "standard_source": {"path": self.standard.relative_to(self.root).as_posix(), "sha256": STANDARD_SHA256, "rows": 9},
        }
        self.write_manifest()

    def write_manifest(self):
        self.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")

    def write_runtime(self, image):
        image.save(self.runtime, format="WEBP", lossless=True, exact=True, method=0)

    def test_reviewed_look_redraw_and_alpha_change_are_allowed(self):
        result = audit(root=self.root)
        self.assertTrue(result["ok"], result["errors"])
        self.assertTrue(result["approved_rgba_equal"])
        self.assertEqual(result["protected_standard_frames"], 57)
        self.assertEqual(result["standard_pixel_mismatches"], 0)
        self.assertNotEqual(load(self.runtime).getpixel(self.LOOK_PIXEL), load(HISTORICAL_WEBP).getpixel(self.LOOK_PIXEL))

    def test_actual_v1_0_0_outline_damage_is_rejected(self):
        result = audit(ROOT / "art/releases/v1.0.0/spritesheet.webp", root=self.root)
        self.assertFalse(result["ok"])
        self.assertGreater(result["source_pixel_mismatches"], 0)
        self.assertGreater(result["standard_pixel_mismatches"], 0)

    def test_runtime_must_match_all_rgba_channels(self):
        for channel, point in (("rgb", self.LOOK_PIXEL), ("alpha", self.LOOK_PIXEL), ("invisible_rgb", (0, 9 * 208))):
            with self.subTest(channel=channel):
                image = load(self.source)
                r, g, b, alpha = image.getpixel(point)
                replacement = (r, g, b, alpha - 1) if channel == "alpha" else ((r + 1) % 256, g, b, alpha)
                image.putpixel(point, replacement)
                self.write_runtime(image)
                result = audit(root=self.root)
                self.assertFalse(result["ok"])
                self.assertEqual(result["source_pixel_mismatches"], 1)
                self.assertEqual(result["standard_pixel_mismatches"], 0)

    def test_reviewed_source_cannot_authorize_changes_to_standard_actions(self):
        image = load(self.source)
        # One of the user's three originally reported damaged hair pixels.
        point = (37, 180)
        self.assertEqual(image.getpixel(point)[:3], (0, 0, 0))
        image.putpixel(point, (1, 0, 0, image.getpixel(point)[3]))
        image.save(self.source)
        self.write_runtime(image)
        self.manifest["source"]["sha256"] = sha(self.source)
        self.write_manifest()
        result = audit(root=self.root)
        self.assertTrue(result["approved_rgba_equal"])
        self.assertFalse(result["ok"])
        self.assertEqual(result["standard_pixel_mismatches"], 1)

    def test_missing_or_changed_approved_source_fails(self):
        self.source.unlink()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Approved source file is missing" in error for error in result["errors"]))
        shutil.copy2(self.standard, self.source)
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Approved source SHA-256 mismatch" in error for error in result["errors"]))

    def test_standard_baseline_and_protected_row_count_are_frozen(self):
        self.standard.unlink()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("Standard source file is missing" in error for error in result["errors"]))
        shutil.copy2(self.reviewed_source, self.standard)
        self.manifest["standard_source"]["sha256"] = sha(self.standard)
        self.write_manifest()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("not the frozen v1.0.1 PNG" in error for error in result["errors"]))
        shutil.copy2(ROOT / "art/releases/v1.0.1/spritesheet.png", self.standard)
        self.manifest["standard_source"]["sha256"] = STANDARD_SHA256
        self.manifest["standard_source"]["rows"] = 8
        self.write_manifest()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("exactly the first 9 rows" in error for error in result["errors"]))

    def test_manifest_is_required_for_new_release_and_version_must_match(self):
        self.manifest_path.unlink()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("required for this release" in error for error in result["errors"]))
        self.manifest["version"] = "v1.0.1"
        self.write_manifest()
        result = audit(root=self.root)
        self.assertFalse(result["ok"])
        self.assertTrue(any("version does not match VERSION" in error for error in result["errors"]))

    def test_unmigrated_v1_0_1_still_uses_historical_audit(self):
        self.manifest_path.unlink()
        (self.root / "VERSION").write_text("v1.0.1\n", encoding="utf-8")
        result = audit(HISTORICAL_WEBP, root=self.root)
        self.assertTrue(result["ok"], result["errors"])
        self.assertEqual(result["mode"], "legacy_v1.0.1_without_manifest")


if __name__ == "__main__":
    unittest.main()
