import unittest
import io, sys

from assignment_1 import *

def capture_print_output(func):
    def inner(*args, **kwargs):
        out = io.StringIO()
        sys.stdout = out
        func(*args, **kwargs)
        sys.stdout = sys.__stdout__
        return out.getvalue().strip()
    return inner




class TestHello(unittest.TestCase):
    def test_print(self):
        capture_print_output
        ans = capture_print_output(hello_world)()
        print(ans)
        self.assertTrue(ans =="hello", "You did not print 'hello'.")

if __name__ == "__main__":
    unittest.main()