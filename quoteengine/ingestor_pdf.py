"""Implementation of PDF stragety for ingestor class."""
from typing import List
from subprocess import run
from os.path import splitext
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """Implements TXT strategy."""

    _supported_files = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the PDF file and return List of QuoteMode."""
        if not cls.can_ingest(path):
            return []
        try:
            run(["pdftotext", "-layout", "-eol", "unix", path], check=True)
            newpath_tuple = splitext(path)
            new_path = newpath_tuple[0] + '.txt'
            quotemode_list = []

            with open(new_path) as file:
                for line in file.readlines():
                    if len(line) > 1:
                        # this line may be re-factored consider regexx
                        row = line.strip().split('-')
                        quote_author = QuoteModel(
                            row[0].strip(),
                            row[1].strip())
                        quotemode_list.append(quote_author)
            return quotemode_list

        except FileNotFoundError as exc:
            print(f'PDF cannot be found {exc}')
            return []
        except IndexError as exc:
            print(f'PDF cannot be read - wrong file structure {exc}')
            return []
