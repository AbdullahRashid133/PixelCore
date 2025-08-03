# test_pixelcore.py
"""
Tests for PixelCore module.
"""

import unittest
from pixelcore import PixelCore

class TestPixelCore(unittest.TestCase):
    """Test cases for PixelCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PixelCore()
        self.assertIsInstance(instance, PixelCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PixelCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
