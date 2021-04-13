"""
Interface used for flexible import of quotes from different sources.

We will have more comments here.
"""
from abc import ABC, abstractmethod
from typing import List
from .quote_mode import QuoteMode


class IngestorInterface(ABC):
    """Abstract classs used Data Source for Quotes."""
    _supported_files = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file extensions is supported."""
        return path.split()[-1] in cls.supported_files

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parse the file and returns List of QuoteModel Objects."""

    @classmethod
    def supported_files(cls) -> List[str]:
        """Return supported files List."""
        return cls._supported_files
