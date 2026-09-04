# test_shardprime.py
"""
Tests for ShardPrime module.
"""

import unittest
from shardprime import ShardPrime

class TestShardPrime(unittest.TestCase):
    """Test cases for ShardPrime class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShardPrime()
        self.assertIsInstance(instance, ShardPrime)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShardPrime()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
