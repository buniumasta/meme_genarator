"""Meme generator Engine."""


class MemeEngine():
    """MemeEngine class generates meme on pictures."""

    def __init__(self, output_dir: str):
        """Initialize MemeEngine Object."""
        self._output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Make meme and return generated image path."""

    @property
    def output_dir(self) -> str:
        """Return output_dir."""
        return self._output_dir
