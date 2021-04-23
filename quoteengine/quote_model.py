"""Module defines QuoteMode class."""


class QuoteModel:
    """Class stores quote and author."""

    def __init__(self, body: str = "", author: str = ""):
        """Initialize QuoteMode Objects."""
        self._body = body
        self._author = author
        self.add_line(25)

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

    def add_line(self, max_length):
        """Split body into lines."""
        if len(self.body) > max_length:
            words = self.body.split(' ')
            word_len = 0
            linebreak = 0
            for index, word in enumerate(words):
                word_len += len(word) + 1
                if word_len > max_length:
                    linebreak = index
            if linebreak > 0:
                words.insert(linebreak,'\n')
                self.body = ' '.join(words)
