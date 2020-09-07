#!/usr/bin/env python3.8
from account import   Account
from credential import Credential
from termcolor import colored,cprint
import os
import time


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

  login=False #Set initial login value to false 

  def display_title():
    os.system('clear')
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
          ""","magenta")

  display_title()


  while login==False:
    cprint("""
      Use the following short codes to manage your password locker account 
          'ln' - Login 
          'xx' - Close app
          ""","blue")
    cprint("\tWhat would you like to do?",'cyan')
    s_code = input().lower()
    if s_code=='ln':
      cprint('\tDo you have an account? Y/N','cyan')
      acc_code=input().upper()
      if acc_code=='Y':
        cprint('\tEnter your username and password  to login >>>\n','blue')
        login_user_name=input('\tEnter username >> ')
        login_password=input('\tEnter password >> ')
        print("\n\t\tSigning in...")
        time.sleep(1.5)
        if auth_user(login_user_name,login_password):
          cprint('\n\t\tLOGIN SUCCESSFUL','green',attrs=['bold'])  
          login=True
        else:
          cprint('\n\t\tSORRY COULD NOT VERIFY USER','red',attrs=['bold'])  

      elif acc_code=='N':
        cprint('\tEnter your username,firstname,lastname and password  to register account >>>\n','blue')
        reg_user_name=input('\tEnter username >> ')
        reg_f_name=input('\tEnter firstname >> ')
        reg_l_name=input('\tEnter lastname >> ')
        reg_password=input('\tEnter password >> ')
        print("\n\t\tRegistering ...")
        time.sleep(1.5)
        new_acc=create_account(reg_user_name,reg_f_name,reg_l_name,reg_password)
        save_account(new_acc)
        cprint("\n\t\tCONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED","green",attrs=['bold'])
        cprint("\n\tSign into your new account","blue")
        sign_username=input('\n\tEnter username >> ')
        sign_password=input('\n\tEnter password >> ')
        print("\n\t\tSigning in ...")
        time.sleep(1.5)
        if auth_user(sign_username,sign_password):
          cprint("\n\t\tLOGIN SUCCESSFUL","green",attrs=['bold'])
          login=True
        else :
          cprint('\n\t\tSORRY COULD NOT VERIFY USER','red',attrs=['bold'])  
      else:
        cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES','red',attrs=['bold'])  
    elif s_code=='xx':
      break
    else:
      cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES','red',attrs=['bold'])  

  
  while  login==True:
    print('LOGGED IN')
if __name__ == '__main__':

    main()    




