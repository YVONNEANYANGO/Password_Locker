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

