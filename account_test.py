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


  def test_save_account(self):
    '''
    test_save_account test case to test if the account object is saved into
    the accounts list
    '''
    self.new_account.save_account()
    self.assertEqual(len(Account.accounts_list),1)    

  def test_get_login_dets(self):
    '''
    method that returns accounts info to use during test_get_login_dets
    '''
    self.new_account.save_account()
    account=Account.get_login_dets()
    self.assertEqual(self.new_account.user_name,account.user_name)

    
if __name__ == '__main__':
    unittest.main()           

    