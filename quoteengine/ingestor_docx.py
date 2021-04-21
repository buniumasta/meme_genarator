"""Implementation of Docx stragety for ingestor class."""
from typing import List
from docx import Document
from docx import opc
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class DOCXIngestor(IngestorInterface):
    """Implements CSV strategy."""

    _supported_files = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file and return List of QuoteMode."""
        if not cls.can_ingest(path):
            return []

        try:
            document = Document(path)
            quotemode_list = []
            for line in document.paragraphs:
                if line.text != "":
                    elems = line.text.split(' - ')
                    # print(elems)
                    quote_author = QuoteModel(
                        elems[0].strip(),
                        elems[1].strip())
                    quotemode_list.append(quote_author)
            return quotemode_list

        except opc.exceptions.PackageNotFoundError:
            print(f'File: "{path}" cannot be found, docx will '
                  'not be processed')
            return []
        except IndexError:
            print(f'File: "{path}" cannot be parsed - wrong file structure')
            return []
