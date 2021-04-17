"""Implementation of DOCx stragety for ingestor class."""
from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Implements DOCX strategy."""

    _supported_files = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given file type and return List of QuoteMode."""
        if not cls.can_ingest(path):
            print('File not known')
            return []

        # data_frame = pd.read_csv(path, header=0)
        # quotemode_list = []
        
        for _, row in data_frame.iterrows():
            quote_author = QuoteModel(row['body'], row['author'])
            quotemode_list.append(quote_author)
        return quotemode_list
