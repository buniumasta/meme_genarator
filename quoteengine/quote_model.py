"""Module defines QuoteMode class."""


class QuoteModel:
    """Class stores quote and author."""

    def __init__(self, body: str = "", author: str = ""):
        """Initialize QuoteMode Objects."""
        self._body = body
        self._author = author

    @property
    def body(self) -> str:
        """Return quote."""
        return self._body

    @property
    def author(self) -> str:
        """Return author."""
        return self._author

    @body.setter
    def body(self, body: str):
        """Set quote."""
        self._body = body

    @author.setter
    def author(self, author: str):
        """Set author."""
        self._author = author

    def __str__(self):
        """Convert object to string."""
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        """Object Representation."""
        return f'"{self.body}" - {self.author}'
