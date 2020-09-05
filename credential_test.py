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


    def test_init(self):
      '''
      Test case to test if object was initialized properly
      '''
      self.assertEqual(self.new_credential.page_name,'twitter')
      self.assertEqual(self.new_credential.pass_word,'qwerty1234')


if __name__ == '__main__':
    unittest.main()           
    