"""Implementation of CSV stragety for ingestor class."""
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class TXTIngestor(IngestorInterface):
    """Implements TXT strategy."""

    _supported_files = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the TXT file and return List of QuoteMode."""
        if not cls.can_ingest(path):
            return []
        quotemode_list = []
        try:
            with open(path, encoding='utf-8-sig') as file:
                for line in file.readlines():
                    row = line.strip().split('-')
                    quote_author = QuoteModel(row[0].strip(), row[1].strip())
                    quotemode_list.append(quote_author)
            return quotemode_list

        except FileNotFoundError:
            print(f'File: "{path}" cannot be found, txt will not be processed')
            return []
        except IndexError:
            print(f'File: "{path}" cannot be parsed - wrong file structure')
            return []
