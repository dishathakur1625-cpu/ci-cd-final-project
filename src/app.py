"""
app.py - Sample counter application for CI/CD pipeline demonstration.
"""


class Counter:
    """A simple counter class for demonstration purposes."""

    def __init__(self, initial_value=0):
        """Initialize counter with an optional starting value."""
        self.count = initial_value

    def increment(self):
        """Increment the counter by 1."""
        self.count += 1
        return self.count

    def decrement(self):
        """Decrement the counter by 1."""
        self.count -= 1
        return self.count

    def reset(self):
        """Reset the counter to zero."""
        self.count = 0
        return self.count

    def get_value(self):
        """Return the current counter value."""
        return self.count
