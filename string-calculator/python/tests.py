import unittest
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

    
        
        
if __name__ == '__main__':
    unittest.main()
