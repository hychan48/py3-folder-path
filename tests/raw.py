import unittest

from a.b.b1 import hello_world
class MyTestCase(unittest.TestCase):
    def test_something(self):
        out = hello_world()
        self.assertEqual(out, "Hello World")  # add assertion here


if __name__ == '__main__':
    unittest.main()
