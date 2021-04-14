"""Test module for quote mode object."""

import unittest
from .quote_model import QuoteModel


class QuoteModeTest(unittest.TestCase):
    """Test Quote Mode Class."""

    def setUp(self):
        """Set up Test Environment."""

    def test_basic(self):
        """Test to.string and initialization."""
        testcase = str(QuoteModel(
            'Take care of all your memories.',
            'Bob Dylan'))
        expected = '"Take care of all your memories." - Bob Dylan'
        self.assertEqual(testcase, expected)
