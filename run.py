#!/usr/bin/env python3.6
from password import Credential

def create_credential(account_name,user_name,email_address,password):
    """
    Function to create a new credential
    """

    new_credential = Credential(account_name,user_name,email_address,password)
    return new_credential


def save_credentials(Credential):
    """
    Function to save credential
    """
    Credential.save_credential()


def del_credential(credential):
    """
    Function to delete a credential
    """
    credential.delete_credential()


def find_credential(name):
    """
    Function that finds a credential by user name and returns the credential
    """
    return Credential.find_by_name(name)


def check_existing_credentials(name):
    """
    Function that check if a credential exists with that user name and return a Boolean
    """
    return Credential.credential_exist(name)


def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credentials()

def main():
    print("Hello Welcome to your PASSWORD-LOCKER account . What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print("\n")

    while True:
        print(" Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit the credential list, ")

        short_code = input().lower()

        if short_code == "cc":
                print("New Credential")
                print("-"*10)

                print("Account Name ....")
                account_name = input()

                print("User Name ....")
                user_name = input()

                print("Email Address ....")
                email_address = input()

                print("Password ....")
                password = input()

                save_credentials(create_credential(account_name,user_name,email_address,password)) # create and save new credential
                print ("\n")
                print(f"New Credential {account_name} {user_name} created")
                print("\n")

        elif short_code == "dc":
                if display_credentials():
                        print('Here is a list of all your credentials')
                        print("\n")
                        for credential in display_credentials():
                            print(f"{credential.account_name} {credential.user_name} .....{credential.email_address} ")
                            print("\n")
                else:
                            print("\n")
                            print("You don't seem to have any credentials saved yet")
                            print("\n")
        elif short_code == "fc":

                print("Enter the user name you want to search for")
                search_name = input()
                if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"{search_credential.account_name} {search_credential.user_name}")
                            print("-" *20)
                            print(f"User name ......{search_credential.user_name}")
                            print(f"Email address .....{search_credential.email}")
                else:
                            print("That credential does not exist")
        elif short_code == "ex":
                print("Bye ......")
                break
        else:
                print("The code wasn't clear. Kindly use short codes")


if __name__ == "__main__":

    main()
