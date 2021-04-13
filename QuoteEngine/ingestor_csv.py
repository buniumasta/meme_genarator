"""Implementation of CSV stragety for ingestor class."""
from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_mode import QuoteMode


class CSVIngestor(IngestorInterface):
    """Implements CSV strategy."""

    _supported_files = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteMode]:
        """Parse the given file type and return List of QuoteMode."""
        if not cls.can_ingest(path):
            print('File not known')
            return []

        data_frame = pd.read_csv(path, header=0)
        quotemode_list = []
        for _, row in data_frame.iterrows():
            quote_author = QuoteMode(row['body'], row['author'])
            quotemode_list.append(quote_author)
        return quotemode_list
