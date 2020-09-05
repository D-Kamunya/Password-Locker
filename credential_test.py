import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_credential=Credential('twitter','qwerty1234')

    def tearDown(self):
      '''
      tearDown method that does clean up after each test case has run.
      '''
      Credential.credentials_list = []


    def test_init(self):
      '''
      Test case to test if object was initialized properly
      '''
      self.assertEqual(self.new_credential.page_name,'twitter')
      self.assertEqual(self.new_credential.pass_word,'qwerty1234')


    def test_save_credential(self):
      '''
      Test case to test if credential object is save intoo credentials_list
      '''
      self.new_credential.save_credential()
      self.assertEqual(len(Credential.credentials_list),1)


    def test_save_mult_credentials(self):
      '''
      Test case to test if we can save multiple credentials_list
      ''' 
      self.new_credential.save_credential()
      test_credential=Credential('instagram','moringa1234')
      test_credential.save_credential()
      self.assertEqual(len(Credential.credentials_list),2)   

if __name__ == '__main__':
    unittest.main()           
    