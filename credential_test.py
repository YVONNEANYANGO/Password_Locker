import unittest # Importing the unittest module 
from password import Credential # Importing the credential class
import pyperclip

class TestCredential(unittest.TestCase):

    """
    Test class defines test cases for the credential class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """


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
            if Credential.user_name == name:
                return credential
    

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


    @classmethod
    def copy_email(cls,name):
        credential_found = Credential.find_by_name(name)
        pyperclip.copy(credential_found.email)

    
    

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("Facebook","Yvonnah Bonswuh","ivonnahbonswuh@gmail.com","ivy1996") # create credential object


    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.account_name,"Facebook")
        self.assertEqual(self.new_credential.user_name,"Yvonnah Bonswuh")
        self.assertEqual(self.new_credential.email_address,"ivonnahbonswuh@gmail.com")
        self.assertEqual(self.new_credential.password,"ivy1996")


    def test_save_credential(self):
        """
        test_save_credential test case to test if the credential object is saved into the credential list
        """
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)


    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []


    def test_save_multiple_credential(self):
        """
        test_save_credential to check if we can save multiple credential objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","Chris","chinjesco@gmail.com","chris1") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
        """
        test_delete_contact to test if we can remove a contact from our contact list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","Chris","chinjesco@gmail.com","chris1") # new credential
        test_credential.save_credential()
        self.new_credential.delete_credential() # Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)


    def test_find_credential_by_user_name(self):
        """
        test to check if we can find a credential of a person by using the user name
        """
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","Chris","chinjesco@gmail.com","chris1") # new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_user_name("Chris")
        self.assertEqual(found_credential.email_address,test_credential.email_address)


    def test_credential_exists(self):
        '''
        Test to check if we can return a Boolean if we can not find the contact.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Facebook","Chris","chinjesco@gmail.com","chris1") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Chris")

        self.assertTrue(credential_exists)


    def test_display_all_credentials(self):
        """
        method that returns a list of all credentials saved 
        """


        self.assertEqual(Credential.display_credentials(),Credential.credential_list)


    def test_copy_email(self):
        """
        Test to confirm that we are copying the email address from a found credential
        """


        self.new_credential.save_credential()
        Credential.copy_email("Chris")

        self.assertEqual(self.new_credential.email,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()
