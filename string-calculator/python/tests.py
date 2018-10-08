import unittest
from calculator import NegativeNumberException
import calculator
class TestStringCalculator(unittest.TestCase):

    def test_method_takes_0_numbers(self):
        result = calculator.Add("")
        self.assertEqual(result, 0)

    def test_method_takes_1_number(self):
        result = calculator.Add("1")
        self.assertEqual(result, 1)

    def test_numbers_greater_than_1000_are_ignored(self):
        result = calculator.Add("2,1001")
        self.assertEqual(result, 2)

    def test_newlines_delim_is_supported(self):
        result = calculator.Add("2\n3\n\n4")
        self.assertEqual(result, 9)

    def test_multiple_delims_in_same_input_are_supported(self):
        result = calculator.Add("1\n2,3")
        self.assertEqual(result, 6)
        
    def test_method_parses_delim_specified_explicitly(self):
        result = calculator.Add('//;\n1;2')
        self.assertEqual(result,3)

    def test_method_parses_delim_within_brackets(self):
        result = calculator.Add('//[-]\n1-2-3')
        self.assertEqual(result,6)

    def test_method_parses_multiple_delims_within_brackets(self):
        result = calculator.Add('//[-][%]\n1-2%3')
        self.assertEqual(result,6)

    def test_method_throws_exception_with_negative_numbers(self):
        with self.assertRaises(NegativeNumberException):
            calculator.Add('1,-1,2')
 
if __name__ == '__main__':
    unittest.main()
