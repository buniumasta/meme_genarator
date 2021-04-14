"""Test Image_caption module."""

import unittest
from .image_caption import ImageCaption


class TestImageCaption(unittest.TestCase):
    """Tests Image_caption class."""

    def test_image_file_1(self):
        """Basic operation test."""
        testcase = str(ImageCaption('./_data/photos/dog/xander_1.jpg'))
        expected = "./_data/photos/dog/xander_1.jpg, JPEG, (500, 500)xRGB"
        self.assertEqual(expected, testcase)

    def test_image_file_2(self):
        """Basic operation test."""
        testcase = str(ImageCaption('./_data/photos/dog/xander_2.jpg'))
        expected = "./_data/photos/dog/xander_2.jpg, JPEG, (500, 500)xRGB"
        self.assertEqual(expected, testcase)

    def test_image_file_3(self):
        """Basic operation test."""
        testcase = str(ImageCaption('./_data/photos/dog/xander_3.jpg'))
        expected = "./_data/photos/dog/xander_3.jpg, JPEG, (500, 500)xRGB"
        self.assertEqual(expected, testcase)

    def test_image_file_4(self):
        """Basic operation test."""
        testcase = str(ImageCaption('./_data/photos/dog/xander_4.jpg'))
        expected = "./_data/photos/dog/xander_4.jpg, JPEG, (500, 500)xRGB"
        self.assertEqual(expected, testcase)

    def test_image_file_empty(self):
        """Basic operation test."""
        testcase = str(ImageCaption('./_data.jpg'))
        expected = ""
        self.assertEqual(expected, testcase)

    def test_check_resize_small(self):
        """Check condition for resize with narrower."""
        image = ImageCaption('./_data/photos/dog/xander_4.jpg')
        self.assertTrue(image.resize_needed(400))

    def test_check_resize_equal(self):
        """Check condition for resize with equal"""
        image = ImageCaption('./_data/photos/dog/xander_4.jpg')
        self.assertFalse(image.resize_needed(500))

    def test_check_resize_bigger(self):
        """Check condition for resize wider"""
        image = ImageCaption('./_data/photos/dog/xander_4.jpg')
        self.assertTrue(image.resize_needed(600))
