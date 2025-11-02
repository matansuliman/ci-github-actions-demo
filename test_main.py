import unittest
from main import simple_function

class TestMain(unittest.TestCase):
    def test_simple_function(self):
        result = simple_function(x=0, a=1, b=2, c=3)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()