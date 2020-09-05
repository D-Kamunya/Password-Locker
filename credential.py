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
