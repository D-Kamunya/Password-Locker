class Account:
  """
  Class that generates an instance of an account
  """
  def __init__(self,user_name,first_name,last_name,pass_word):
    '''
    __init__ method that helps us define properties for our objects.

    Args:
        user_name:Account user login user name
        first_name: Account user login first name.
        last_name : Account user login last name.
        pass_word:Account user login password
    '''
    self.user_name=user_name
    self.first_name=first_name
    self.last_name=last_name
    self.pass_word=pass_word
      
