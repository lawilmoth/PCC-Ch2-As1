import unittest
from cpo import capture_print_output 

from assignment_1 import *


class TestHello(unittest.TestCase):
    def test_print_hello(self):
        #capture_print_output
        ans = capture_print_output(hello_world)()
        
        self.assertTrue(ans =="hello", "You did not print 'hello'.")

class TestProblem1(unittest.TestCase):
    def test_start_with_hello(self):

        ans = capture_print_output(problem_one)()
        
        self.assertTrue(ans[0:5] =="Hello", "The output should start by writing 'Hello'")
    def test_ends_with_name (self):

        ans = capture_print_output(problem_one)()
        
        self.assertGreater(ans, "Hello", "Be sure to output more than just hello")
    def test_hello_name (self):

        ans = capture_print_output(problem_one)()
        var = problem_one()
        self.assertEqual(ans, f"Hello {var}", "The output should say Hello plus your name")

class TestProblem2(unittest.TestCase):
    
    def test_x_wasnt_changed(self):

        x, ls, rs, s = problem_two()
        self.assertEqual(
            x, "                               \t\t          \n          <( o-o )>\n\n\t\t\t          \t", "Don't modify 'x'"
            )
        
    def test_ls (self):
        x, ls, rs, s = problem_two()
        self.assertEqual(
            ls, "<( o-o )>\n\n\t\t\t          \t", "use lstrip()"
            )
        
    def test_rs (self):
        x, ls, rs, s = problem_two()
        self.assertEqual(
            rs, "                               \t\t          \n          <( o-o )>", "use rstrip()"
            )
        
    def test_s (self):
        x, ls, rs, s = problem_two()
        self.assertEqual(
            s, "<( o-o )>", "use the normal strip method"
            )
        
        
        
        



if __name__ == "__main__":
    unittest.main()