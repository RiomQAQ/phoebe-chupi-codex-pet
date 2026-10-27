"""Guard the actual reported defect using the two real release images."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from restore_outlines import audit, build, load, sha, SOURCE, PREVIOUS, WEBP, HISTORICAL_WEBP


class OutlineRegression(unittest.TestCase):
    def test_previous_release_is_rejected(self):
        result = audit(ROOT / "art/releases/v1.0.0/spritesheet.webp")
        self.assertFalse(result["ok"])
        self.assertGreater(result["dark_ink_mismatches"], 0)
        self.assertTrue(result["alpha_and_pose_registration_unchanged"])

    def test_reported_hair_pixels_are_restored(self):
        expected, repaired, current, previous = load(SOURCE), load(HISTORICAL_WEBP), load(WEBP), load(PREVIOUS)
        for row, col, x, y, rgb in [
            (0, 0, 37, 180, (0, 0, 0)),
            (1, 3, 155, 73, (7, 0, 0)),
            (2, 7, 138, 108, (8, 1, 0)),
        ]:
            position = (col * 192 + x, row * 208 + y)
            self.assertEqual(repaired.getpixel(position), expected.getpixel(position))
            self.assertEqual(repaired.getpixel(position)[:3], rgb)
            self.assertEqual(current.getpixel(position), expected.getpixel(position))
            self.assertNotEqual(previous.getpixel(position)[:3], rgb)

    def test_all_pose_and_blink_geometry_is_preserved(self):
        self.assertEqual(load(PREVIOUS).getchannel("A").tobytes(), load(HISTORICAL_WEBP).getchannel("A").tobytes())
        self.assertEqual(sha(HISTORICAL_WEBP), "e1971a5c89d073739c4956e04292249385eb47298dd8ce873deb1be6aaf3bdf2")
        self.assertTrue(audit(HISTORICAL_WEBP)["ok"])

    def test_historical_export_cannot_replace_runtime_or_frozen_release(self):
        for destination in (WEBP.parent, ROOT / "art/final", HISTORICAL_WEBP.parent):
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                build(destination)


if __name__ == "__main__":
    unittest.main()
