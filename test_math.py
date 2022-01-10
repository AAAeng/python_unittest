import unittest
from mathoperations import MathOperations

class UnitTestMathOperations(unittest.TestCase):
 
   def test_addition(self):
       '''
       test math addition
       '''
       math_operations = MathOperations()
       result = math_operations.math_addition(2, 2)
       self.assertEqual(result, 4, "The addition should be 4")
 
   def test_subtraction(self):
       '''
       test math subtraction
       '''
       math_operations = MathOperations()
       result = math_operations.math_subtraction(2, 2)
       self.assertEqual(result, 1, "The subtraction should be 0")

 
if __name__ == "__main__":
   unittest.main()