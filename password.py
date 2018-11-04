class Credential:
    """
    Class that generates new instances of user credentials
    """
    credential_list = [] # Empty credential list
 # Init method
    def __init__(self,account_name,user_name,email_address,password):

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
        
    def save_credential(self):
        """
        save_credential method saves credential objects into credential-list
        """

        Credential.credential_list.append(self)

    def delete_credential(self):

        """
        delete_credential method deletes a saved cotact from the credential_list
        """

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_user_name(cls,name):
        """
        Method that takes in a user name and returns a credential that matches that user name
        

        Args:
        user_name: user name to search for 
        Returns:
        Credential of someone who matches the user name.
        """

        for user_name in cls.credential_list:
            if user_name.user_name == name:
                return user_name
    

    @classmethod
    def credential_exist(cls,name):
        """
        Method that checks if a credential exists from the credential list.
        
        Args:
        name: User name to search if it exists
        Returns:
        Boolean: TRue or false depending if the credential exists
        """
        for credential in cls.credential_list:
            if credential.user_name == name:
                return True

        return False


    @classmethod
    def display_credentials(cls):
        """
        method that returns the credential list
        """
        return cls.credential_list