#!/usr/bin/env python3
import unittest
from quote_mode import QuoteMode 

class QuoteModeTest(unittest.TestCase):
    """Test Quote Mode Class."""
    def setUp(self):
        pass

    def test_basic(self):
        testcase = str(QuoteMode('Take care of all your memories.','Bob Dylan'))
        expected = '"Take care of all your memories." - Bob Dylan'
        self.assertEqual(testcase, expected)
    

if __name__ == '__main__':
    unittest.main()