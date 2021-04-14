"""Test ingestor interace class implementation."""
import unittest
from .ingestor import Ingestor
from .test_helper import get_csvfile_quotemode


class TestIngestor(unittest.TestCase):
    """Test class for CSVIngestor implementation."""

    def test_csv_file_import(self):
        """Testing import from csv file."""
        list_test = Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
        test_case = [str(x) for x in list_test]
        expected = get_csvfile_quotemode()
        self.assertEqual(expected, test_case)