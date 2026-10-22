"""Guard the actual reported defect using the two real release images."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from restore_outlines import audit, load, SOURCE, PREVIOUS, WEBP


class OutlineRegression(unittest.TestCase):
    def test_previous_release_is_rejected(self):
        result = audit(ROOT / "art/releases/v1.0.0/spritesheet.webp")
        self.assertFalse(result["ok"])
        self.assertGreater(result["dark_ink_mismatches"], 0)
        self.assertTrue(result["alpha_and_pose_registration_unchanged"])

    def test_reported_hair_pixels_are_restored(self):
        expected, repaired, previous = load(SOURCE), load(WEBP), load(PREVIOUS)
        for row, col, x, y, rgb in [
            (0, 0, 37, 180, (0, 0, 0)),
            (1, 3, 155, 73, (7, 0, 0)),
            (2, 7, 138, 108, (8, 1, 0)),
        ]:
            position = (col * 192 + x, row * 208 + y)
            self.assertEqual(repaired.getpixel(position), expected.getpixel(position))
            self.assertEqual(repaired.getpixel(position)[:3], rgb)
            self.assertNotEqual(previous.getpixel(position)[:3], rgb)

    def test_all_pose_and_blink_geometry_is_preserved(self):
        self.assertEqual(load(PREVIOUS).getchannel("A").tobytes(), load(WEBP).getchannel("A").tobytes())
        self.assertTrue(audit(WEBP)["ok"])


if __name__ == "__main__":
    unittest.main()
