"""The main ingestor strategy class module."""
from typing import List
from .quote_model import QuoteModel
from .ingestor_csv import CSVIngestor
from .ingestor_docx import DOCXIngestor
from .ingestor_txt import TXTIngestor
from .ingestor_interface import IngestorInterface


class Ingestor(IngestorInterface):
    """Strategy object importing from all known soruces."""

    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given file type and return List of QuoteMode."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
        raise ValueError(f"StrategyIngestor: file type not supported {path}")
