"""Test ingestor interace class implementation."""
import unittest
from .ingestor_pdf import PDFIngestor
from .test_helper import get_pdffile_dog
# from .test_helper import get_csvfile_art


class TestPDFIngestor(unittest.TestCase):
    """Test class for PDFIngestor implementation."""

    def test_pdf_dog_import(self):
        """Testing import from pdf file."""
        list_test = PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')
        test_case = [str(x) for x in list_test]
        expected = get_pdffile_dog()
        self.assertEqual(expected, test_case)

    # def test_csv_art_import(self):
    #     """Testing import from csv file."""
    #     list_test = CSVIngestor.parse('./_data/ArtQuotes/ArtQuotesCSV.csv')
    #     test_case = [str(x) for x in list_test]
    #     expected = get_csvfile_art()
    #     self.assertEqual(expected, test_case)
    #     # add the test to check raise error if not proper file is there.
    #     # add the test to check if wrong file is not read etc...
