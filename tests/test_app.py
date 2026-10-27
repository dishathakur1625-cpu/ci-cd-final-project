"""
test_app.py - Unit tests for the Counter application.
"""
import sys
import os
import unittest

# Ensure the src directory is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import Counter  # noqa: E402


class TestCounter(unittest.TestCase):
    """Test cases for the Counter class."""

    def setUp(self):
        """Set up a fresh Counter before each test."""
        self.counter = Counter()

    def test_initial_value_is_zero(self):
        """Counter should start at zero by default."""
        self.assertEqual(self.counter.get_value(), 0)

    def test_increment(self):
        """Counter should increment by 1."""
        self.counter.increment()
        self.assertEqual(self.counter.get_value(), 1)

    def test_decrement(self):
        """Counter should decrement by 1."""
        self.counter.increment()
        self.counter.increment()
        self.counter.decrement()
        self.assertEqual(self.counter.get_value(), 1)

    def test_reset(self):
        """Counter should reset to zero."""
        self.counter.increment()
        self.counter.increment()
        self.counter.reset()
        self.assertEqual(self.counter.get_value(), 0)

    def test_initial_custom_value(self):
        """Counter should accept a custom initial value."""
        counter = Counter(initial_value=10)
        self.assertEqual(counter.get_value(), 10)

    def test_multiple_increments(self):
        """Counter should handle multiple increments correctly."""
        for _ in range(5):
            self.counter.increment()
        self.assertEqual(self.counter.get_value(), 5)

    def test_multiple_decrements(self):
        """Counter should handle multiple decrements correctly."""
        self.counter.count = 5
        for _ in range(3):
            self.counter.decrement()
        self.assertEqual(self.counter.get_value(), 2)


if __name__ == '__main__':
    unittest.main()
