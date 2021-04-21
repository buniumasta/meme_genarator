"""Implementation of CSV stragety for ingestor class."""
from typing import List
import pandas as pd
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Implements CSV strategy."""

    _supported_files = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file and return List of QuoteMode."""
        try:
            if not cls.can_ingest(path):
                return []

            data_frame = pd.read_csv(path, header=0)
            quotemode_list = []
            for _, row in data_frame.iterrows():
                quote_author = QuoteModel(row['body'], row['author'])
                quotemode_list.append(quote_author)
            return quotemode_list

        except FileNotFoundError:
            print(f'File: "{path}" cannot be found, csv will not be processed')
            return []
        except IndexError:
            print(f'File: "{path}" cannot be parsed - wrong file structure')
            return []
