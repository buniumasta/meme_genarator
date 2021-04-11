"""
Interface used for flexible import of quotes from different sources.

We will have more comments here.
"""
from abc import ABC, abstractmethod
from typing import List
from .quote_mode import QuoteMode


class IngestorInterface(ABC):
    """Abstract classs used Data Source for Quotes."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file extensions is supported."""
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parse the file and returns List of QuoteModel Objects."""
        pass
