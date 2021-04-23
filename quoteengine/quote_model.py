"""Module defines QuoteMode class."""


class QuoteModel:
    """Class stores quote and author."""

    def __init__(self, body: str = "", author: str = ""):
        """Initialize QuoteMode Objects."""
        self._body = body
        self._author = author
        self.add_line(28)

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
            linebreaks = []
            for index, word in enumerate(words):
                word_len += len(word) + 1
                if word_len > max_length:
                    linebreaks.append(index)
                    word_len = 0
            if len(linebreaks) > 0:
                added_breaks=0
                for linebreak in linebreaks:
                    words.insert(linebreak+added_breaks+1,'\n')
                    added_breaks+=1
                self.body = ' '.join(words)
