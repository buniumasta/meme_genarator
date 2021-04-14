"""
Interface used for flexible import of quotes from different sources.

We will have more comments here.
"""
from abc import ABC, abstractmethod
from typing import List
from .quote_mode import QuoteMode


class IngestorInterface(ABC):
    """Abstract classs used as Data Source for Quotes."""

    _supported_files = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file extensions is supported."""
        ext = path.split('.')[-1]
        # This statetement below needs to be refactored, 
        # after adding all options.
        if ext in cls._supported_files:
            # print(f'{ext} is in supported file types')
            return True
        # print(f'{path.split()[-1]} is NOT in supported file types')
        return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parse the file and returns List of QuoteMode Objects."""

    # @property
    # def supported_files(self) -> List[str]:
    #     """Return supported files List."""
    #     return self._supported_files
