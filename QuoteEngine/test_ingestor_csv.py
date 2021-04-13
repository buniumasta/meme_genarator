"""Test ingestor interace class implementation."""
import unittest
from .ingestor_csv import CSVIngestor
from .quote_mode import QuoteMode


class Test_CSVIngestor(unittest.TestCase):
    """Test class for CSVIngestor implementation."""

    def test_csv_file_import(self):
        """Testing import from csv file."""
        list_test = CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
        test_case = [str(x) for x in list_test]
        expected = [
            str(QuoteMode('Chase the mailman', 'Skittle')),
            str(QuoteMode('When in doubt, go shoe-shopping', 'Mr. Paws'))]
        self.assertEqual(expected, test_case)
