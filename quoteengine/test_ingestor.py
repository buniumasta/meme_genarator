"""Test ingestor interace class implementation."""
import unittest
from .ingestor import Ingestor
from .test_helper import get_csvfile_dog
from .test_helper import get_docxfile_dog
from .test_helper import get_txtfile_dog
from .test_helper import get_pdffile_dog


class TestIngestor(unittest.TestCase):
    """Test class for CSVIngestor implementation."""

    def testf_csv_file_import(self):
        """Testing import from csv file."""
        list_test = Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
        test_case = [str(x) for x in list_test]
        expected = get_csvfile_dog()
        self.assertEqual(expected, test_case)
        # Add test for empty file.

    def testf_docx_file_import(self):
        """Testing import from docx file."""
        list_test = Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx')
        test_case = [str(x) for x in list_test]
        expected = get_docxfile_dog()
        self.assertEqual(expected, test_case)

    def testf_txt_file_import(self):
        """Testing import from txt file."""
        list_test = Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt')
        test_case = [str(x) for x in list_test]
        expected = get_txtfile_dog()
        self.assertEqual(expected, test_case)

    # def testf_pdf_file_import(self):
    #     """Testing import from pdf file."""
    #     list_test = Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')
    #     test_case = [str(x) for x in list_test]
    #     expected = get_pdffile_dog()
    #     self.assertEqual(expected, test_case)
