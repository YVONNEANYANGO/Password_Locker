import unittest # Importing the unittest module 
from credential import Credential # Importing the credential class

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
        self.new_contact = Contact("Facebook","Yvonnah Bonswuh","ivonnahbonswuh@gmail.com","ivy1996") # create credential object


    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.account_name,"Facebook")
        self.assertEqual(self.new_credential.user_name,"Yvonnah Bonswuh")
        self.assertEqual(self.new_credential.email_address,"ivonnahbonswuh@gmail.com")
        self.assertEqual(self.new_credential.password,"ivy1996")


if __name__ == '__main__':
    unittest.main()
