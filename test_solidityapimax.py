# test_solidityapimax.py
"""
Tests for SolidityAPIMax module.
"""

import unittest
from solidityapimax import SolidityAPIMax

class TestSolidityAPIMax(unittest.TestCase):
    """Test cases for SolidityAPIMax class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolidityAPIMax()
        self.assertIsInstance(instance, SolidityAPIMax)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolidityAPIMax()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
