"""Module defines image with caption capability."""
import os
from PIL import Image

class ImageCaption():
    """Image class."""

    def __init__(self, image_path):
        """Initialize image caption object."""
        self.image_path = image_path
        try:
            with Image.open(image_path) as self.image:
                path = os.getcwd()
        except OSError:
            self.image = None
            print(f'Cannot open:{image_path}, current working directory: {path}')

    def image_resize(self, width: str):
        """Re-size image to width."""

    def add_caption(self, body: str, author: str):
        """Add caption to an image with random place."""

    def __str__(self):
        """Provide information about the picture."""
        return f'{self.image_path}, {self.image.format},' \
            f' {self.image.size}x{self.image.mode}'
