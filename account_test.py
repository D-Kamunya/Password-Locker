import unittest
from account import Account

class TestAccount(unittest.TestCase):
  '''
  Test class that defines test cases for the account class behaviours.

  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_account=Account('kinc','Dennis','Kamunya','qwerty1234')


  def test_init(self):
    '''
    Test_init test case to test if the object is initialized properly
    ''' 
    self.assertEqual(self.new_account.user_name,'kinc')
    self.assertEqual(self.new_account.first_name,'Dennis') 
    self.assertEqual(self.new_account.last_name,'Kamunya')  
    self.assertEqual(self.new_account.pass_word,'qwerty1234') 

if __name__ == '__main__':
    unittest.main()           

    