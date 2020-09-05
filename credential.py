class Credential:
  """
  Class that generates an instance of a Credential
  """
  def __init__(self,page_name,pass_word):
    '''
    __init__ method that helps us define properties for our objects.

    Args:
        page_name:Name of page or account you want to save ctedentials fotrt
        pass_word:Password of page you want to save
    '''
    self.page_name=page_name
    self.pass_word=pass_word

  credentials_list=[] #Empty credentials list

  def save_credential(self):
    '''
    Saves credential object in the credentials list
    '''
    Credential.credentials_list.append(self)

  def delete_credential(self):
    '''
    Deletes credential obj from credentials list
    '''
    Credential.credentials_list.remove(self)  

  @classmethod
  def find_by_pagename(cls,pagename):
    '''
    Method that takes in a page name and returns a credential that matches that page name.

    Args:
        pagename: Page name to search for
    Returns :
        Credential that matches the pag ename.
    '''
    for credential in cls.credentials_list:
      if credential.page_name==pagename:
        return credential


  @classmethod
  def credential_exists(cls,pagename):
    '''
    Method that checks if a credential exists from the credential list.
    Args:
        pagename: Page name to search if it exists
    Returns :
        Boolean: True or false depending if the credential exists
    '''
    for credential in cls.credentials_list:
      if credential.page_name==pagename:
        return True

    return False

  @classmethod
  def display_credentials(cls):
    '''
    method that returns the credentials list
    '''
    return cls.credentials_list            
