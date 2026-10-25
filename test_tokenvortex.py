# test_tokenvortex.py
"""
Tests for TokenVortex module.
"""

import unittest
from tokenvortex import TokenVortex

class TestTokenVortex(unittest.TestCase):
    """Test cases for TokenVortex class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenVortex()
        self.assertIsInstance(instance, TokenVortex)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenVortex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
