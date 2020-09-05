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

if __name__ == '__main__':
    unittest.main()           

    