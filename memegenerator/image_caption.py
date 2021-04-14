"""Module defines image with caption capability."""
from PIL import Image


class ImageCaption():
    """Image class."""

    def __init__(self, image_path):
        """Initialize image caption object."""
        self.image_path = image_path
        try:
            self.image = Image.open(image_path)
        except OSError:
            self.image = None

    def image_resize(self, width: str):
        """Re-size image to width."""

    def add_caption(self, body: str, author: str):
        """Add caption to an image with random place."""

    def __str__(self):
        """Provides information about the picture"""
        return  f'{self.image_path}, {self.image.format},\
            {self.image.size}x{self.image.mode}'
