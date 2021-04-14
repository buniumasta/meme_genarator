"""Test Image_caption module."""

import unittest
from .image_caption import ImageCaption


class TestImageCaption(unittest.TestCase):
    """Tests Image_caption class."""

    def test_image_basic(self):
        """basic operation test."""
        testcase = str(ImageCaption('./_data/photos/dog/xander_1.jpg')) 
        expected = "./_data/photos/dog/xander_1.jpg, JPEG, (500, 500)xRGB"
        self.assertEqual(expected, testcase)
