"""Implementation of CSV stragety for ingestor class."""
import panda as pd
from .ingestor_interface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Implements CSV strategy."""

    def __init__(self, path: str):
        """Initialize CSVIngestor class."""

    def can_ingest(self, path: str) -> bool:
        """Check if file can be ingested."""
