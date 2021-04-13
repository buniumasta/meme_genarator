"""Implementation of CSV stragety for ingestor class."""
# import panda as pd
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_mode import QuoteMode


class CSVIngestor(IngestorInterface):
    """Implements CSV strategy."""

    def __init__(self, path: str):
        """Initialize CSVIngestor class."""
        super()
        super.supported_files.append(path.split('.')[-1])

    def parse(self, path: str) -> List[QuoteMode]:
        """Parse the given file type and return List of QuoteMode."""
    
