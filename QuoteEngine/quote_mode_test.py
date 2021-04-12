"""Test module for quote mode object"""

import unittest
from .Quote_mode import QuoteMode

class QuoteModeTest(unittest.TestCase):
    """Test Quote Mode Class."""
    def setUp(self):
        pass

    def test_basic(self):
        """Test to.string and initialization."""
        testcase = str(QuoteMode('Take care of all your memories.','Bob Dylan'))
        expected = '"Take care of all your memories." - Bob Dylan'
        self.assertEqual(testcase, expected)
