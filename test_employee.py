import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    # check email:
    def test_email(self):
        emp_1 = Employee('C', 'S',500)
        emp_2 = Employee('Su', 'Sm',1000)
        
        self.assertEqual(emp_1.email, '{}.{}@email.com'.format('C','S'))
        self.assertEqual(emp_2.email, '{}.{}@email.com'.format('Su','Sm'))
        
        emp_1.first= 'Jh'
        emp_2.first= 'Ja'
        
        self.assertEqual(emp_1.email, 'Jh.S@email.com')
        self.assertEqual(emp_2.email, 'Ja.Sm@email.com')
    
    
    def test_fullname(self):
        emp_1 = Employee('C', 'S',500)
        emp_2 = Employee('Su', 'Sm',1000)
        
        self.assertEqual(emp_1.fullname, '{} {}'.format('C','S'))
        self.assertEqual(emp_2.fullname, '{} {}'.format('Su','Sm'))
        
        emp_1.first= 'Jh'
        emp_2.first= 'Ja'
        
        self.assertEqual(emp_1.fullname, 'Jh S')
        self.assertEqual(emp_2.fullname, 'Ja Sm')


    def test_apply_raise(self):
        emp_1 = Employee('C', 'S',500)
        emp_2 = Employee('Su', 'Sm',1000)
        
        
        emp_1.apply_raise()
        emp_2.apply_raise()
        
        self.assertEqual(emp_1.pay, 525 )
        self.assertEqual(emp_2.pay,1050 )

if __name__=='__main__':
    unittest.main()        
        
        
        
        
                