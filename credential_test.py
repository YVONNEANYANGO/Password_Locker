import unittest # Importing the unittest module 
from password import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    """
    Test class defines test cases for the credential class behaviours.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases
    """


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
        

if __name__ == '__main__':
    unittest.main()
