"""Test ingestor interace class implementation."""
import unittest
from .ingestor_csv import CSVIngestor


class Test_CSVIngestor(unittest.TestCase):
    """Test class for CSVIngestor implementation."""
    @classmethod
    def setUpClass(cls):
        """Initialize class for test."""
        cls.csv_ingestor = CSVIngestor('DogQuotesCSV.csv')

    def test_basic_csv(self):
        """Initialization of class."""
        supported_files = self.csv_ingestor.supported_files
        self.assertIn('csv', supported_files)
