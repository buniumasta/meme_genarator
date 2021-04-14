"""The main ingestor strategy class module."""
from typing import List
from .quote_mode import QuoteMode
from .ingestor_csv import CSVIngestor
from .ingestor_interface import IngestorInterface


class Ingestor(IngestorInterface):
    """Strategy object importing from all known soruces."""

    ingestors = [CSVIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parse the given file type and return List of QuoteMode."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        return []
