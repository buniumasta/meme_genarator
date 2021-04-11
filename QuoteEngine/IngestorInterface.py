"""
Interface used for flexible import of quotes from different sources.
"""
from abc import ABC, abstractmethod
from .QuoteMode import QuoteMode
from typing import List

class IngestorInterface(ABC):
    """Abstract classs used Data Source for Quotes."""

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Checks if file extensions is supported."""
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parses the file and returns List of QuoteModel Objects"""
        pass
