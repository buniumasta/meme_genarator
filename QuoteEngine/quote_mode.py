"""Class stores quote and author."""


class QuoteMode:
    """Class stores quote and author."""

    def __init__(self, quote: str, author: str):
        """Initialize QuoteMode Objects."""
        self._quote = quote
        self._author = author
    @property
    def quote(self) -> str:
        """Return quote."""
        return self._quote
    @property
    def author(self) -> str:
        """Return author."""
        return self._author
    @quote.setter
    def quote(self, quote: str):
        """Set quote."""
        self._quote = quote
    @author.setter
    def author(self, author: str):
        """Set author."""
        self._author = author
    