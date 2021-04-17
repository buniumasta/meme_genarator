"""Implementation of Docx stragety for ingestor class."""
from typing import List
from docx import Document
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Implements CSV strategy."""

    _supported_files = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the given file type and return List of QuoteMode."""
        if not cls.can_ingest(path):
            print('File not known')
            return []

        document = Document('./_data/DogQuotes/DogQuotesDOCX.docx') 
        quotemode_list = []
        for line in document.paragraphs:
            if line != "":
                elems = line.split('_')
                print(elems)
                quote_author = QuoteModel(elems[0].strip(), elems[1].strip())
                quotemode_list.append(quote_author)
        return quotemode_list
