"""Module defines image with caption capability."""
import os
from PIL import Image


class ImageCaption():
    """Image Caption classs"""

    def __init__(self, image_path):
        """Initialize image caption object."""
        self.image_path = image_path
        try:
            with Image.open(image_path) as self.image:
                pass
        except OSError:
            self.image = None

    def image_resize(self, width: int):
        """Re-size image to width."""

    def resize_needed(self, width: int) -> bool:
        """Check if resize is needed"""
        if self.image.size[1] != width:
            return True
        return False

    def add_caption(self, body: str, author: str):
        """Add caption to an image with random place."""

    def __str__(self):
        """Provide information about the picture."""
        if self.image is not None:
            return f'{self.image_path}, {self.image.format},' \
                f' {self.image.size}x{self.image.mode}'
        return ""
