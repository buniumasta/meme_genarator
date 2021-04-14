"""Test ingestor interace class implementation."""
import unittest
from .ingestor_csv import CSVIngestor
from .test_helper import get_csvfile_dog
from .test_helper import get_csvfile_art
# add the test to check raise error if not proper file is there.
# add the test to check if wrong file is not read etc...


class TestCsvIngestor(unittest.TestCase):
    """Test class for CSVIngestor implementation."""

    def test_csv_dog_import(self):
        """Testing import from csv file."""
        list_test = CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv')
        test_case = [str(x) for x in list_test]
        expected = get_csvfile_dog()
        self.assertEqual(expected, test_case)

    def test_csv_art_import(self):
        """Testing import from csv file."""
        list_test = CSVIngestor.parse('./_data/ArtQuotes/ArtQuotesCSV.csv')
        test_case = [str(x) for x in list_test]
        expected = get_csvfile_art()
        self.assertEqual(expected, test_case)
