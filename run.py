#!/usr/bin/env python3.8
from account import   Account
from credential import Credential

'''
Functions that implement the behaviours in account class.
'''
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