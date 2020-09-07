#!/usr/bin/env python3.8
from account import   Account
from credential import Credential
from termcolor import colored,cprint


#Functions that implement the behaviours in account class.

def create_account(username,fname,lname,p_word):
  '''
  Function to create new account
  '''
  new_account=Account(username,fname,lname,p_word)
  return new_account
    

def save_account(account):
  '''
  Function to save account
  '''
  account.save_account()


def delete_account(account):
  '''
  Function to delete an account
  '''
  account.delete_account()


def auth_user(username,password):
  '''
  Function to authenicate user during login
  '''
  return Account.auth_user(username,password) 

#Functions that implement the behaviours in credential class.

def create_credential(page,password):
  '''
  Function to create credentials
  '''
  new_credential=Credential(page,password)
  return new_credential


def save_credential(credential):
  '''
  Function to save credential
  '''
  credential.save_credential()


def delete_credential(credential):
  '''
  Function to delete credential
  '''
  credential.delete_credential()


def find_cred_by_pagename(pagename):
  """
  Function that finds a credential by pagename and returns the credentials
  """
  return Credential.find_by_pagename(pagename)


def check_credential_exists(pagename):
  '''
  Function that check if a credential exists with that pagename and return a Boolean
  '''
  return Credential.credential_exists(pagename)


def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credential.display_credentials()


def generate_password():
  '''
  Function that generte a random password
  '''
  return Credential.generate_password() 


def main():
  def display_title():
    '''
    Function to display app title bar
    '''
    cprint("""
          \n\t\t\t\t**********************************************
          \t\t**************************************************************************
          \t*******************************************************************************************
          \n
          \t\t\t\t        _   |~  _
          \t\t\t\t       [_]--'--[_]
          \t\t\t\t       |'|""`""|'|
          \t\t\t\t       | | /^\ | |
          \t\t\t\t       |_|_|I|_|_|
          \n\t\t\t\t***  GREETINGS USER, WELCOME TO PASSWORD LOCKER  ***
          \n`\t\t\t******************************************************************
          ""","blue")

  display_title()
if __name__ == '__main__':

    main()    




