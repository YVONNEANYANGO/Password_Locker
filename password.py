Class Credential:
"""
Class that generates new instances of user credentials
"""

    def __init__(self,account_name,user_name,email_address,password)

    """
    __init__ method that helps us define properties for our objects
    
        Args:
            account_name: New credential account name.
            user_name: New credential user name.
            email_address: New credential email address.
            password: New credential password.
      """

      self.account_name = account_name
      self.user_name = user_name
      self.email_address = email_address
      self.password = password
