#!/usr/bin/env python3.6
from password import Credential

def create_credential(account_name,user_name,email_address,password):
    """
    Function to create a new credential
    """

    new_credential = Credential(account_name,user_name,email_address,password)
    return new_credential