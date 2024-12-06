import unittest
import calc
 
class TestCase(unittest.TestCase): # access to different Test case within this class
     
     def test_add(self):  
         self.assertEqual(calc.add(10,5), 15)
         
         self.assertEqual(calc.add(-1,1), 0) #edge case 1
         self.assertEqual(calc.add(-1,-1), -2) #edge case 2
         
     # adding more test methods to test more "tests":
     def test_subrtact(self):  
         self.assertEqual(calc.subtract(10,5), 5)    
         self.assertEqual(calc.subtract(-1,1), -2)
         self.assertEqual(calc.subtract(-1,-1), 0)         
     
     def test_multiply(self):  
         self.assertEqual(calc.multiply(10,5), 50)  
         
     def test_divide(self):  
        
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(5,2), 2.5)
        
        # testing exceptions:
        self.assertRaises(ValueError, calc.divide, 10, 2)
        with self.assertRaises(ValueError):
            calc.divide(10,0)
             


if __name__ == '__main__':
    unittest.main()     

         

     