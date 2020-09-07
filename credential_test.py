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

    def test_delete_credential(self):
      '''
      Test case to test if we can remove a credential from our credentials list
      '''
      self.new_credential.save_credential()
      test_credential=Credential('instagram','moringa1234')
      test_credential.save_credential()
      self.new_credential.delete_credential()

      self.assertEqual(len(Credential.credentials_list),1)


    def test_find_by_pagename(self):
      '''
      test to check if we can find a credential by page name and display information
      '''
      self.new_credential.save_credential()  
      test_credential=Credential('instagram','moringa1234')
      test_credential.save_credential()
      found_credential=Credential.find_by_pagename('instagram')

      self.assertEqual(test_credential.page_name,found_credential.page_name)


    def test_credential_exists(self):
      '''
      Test to check if we can return a Boolean  if we cannot find the credential.
      '''
      self.new_credential.save_credential()
      test_credential=Credential('instagram','moringa1234')
      test_credential.save_credential()
      credential_exist=Credential.credential_exists('instagram')

      self.assertTrue(credential_exist)



    def test_display_credentials(self):
      '''
      method that returns a list of all credentials saved
      '''
      self.new_credential.save_credential()
      test_credential=Credential('instagram','moringa1234')
      test_credential.save_credential()
      credentials=Credential.display_credentials()

      self.assertEqual(Credential.credentials_list,credentials) 
    


     

if __name__ == '__main__':
    unittest.main()           
    