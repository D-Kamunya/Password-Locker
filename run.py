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

def create_credential(page,username,password):
  '''
  Function to create credentials
  '''
  new_credential=Credential(page,username,password)
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
  sign_name='' #Name of user currently logged in
  logged=True

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
  while logged:
    display_title()


    while login==False:
      cprint("""
        Use the following short codes to manage your password locker account 
            'ln' - Login 
            'xx' - Close app
            ""","blue")
      s_code = input(colored('\tWhat would you like to do? >> ','cyan')).lower()
      if s_code=='ln':
        acc_code=input(colored('\tDo you have an account? Y/N >> ','cyan')).upper()
        if acc_code=='Y':
          cprint('\tEnter your username and password  to login >>>\n','blue')
          login_user_name=input(colored('\tEnter username >> ','cyan'))
          login_password=input(colored('\tEnter password >> ','cyan'))
          print("\n\t\tSigning in...")
          time.sleep(1.5)
          if auth_user(login_user_name,login_password):
            cprint('\n\t\tLOGIN SUCCESSFUL','green',attrs=['bold'])
            sign_name=login_user_name  
            login=True
          else:
            cprint('\n\t\tSORRY COULD NOT VERIFY USER','red',attrs=['bold'])  

        elif acc_code=='N':
          cprint('\tEnter your username,firstname,lastname and password  to register account >>>\n','blue')
          reg_user_name=input(colored('\tEnter username >> ','cyan'))
          reg_f_name=input(colored('\tEnter firstname >> ','cyan'))
          reg_l_name=input(colored('\tEnter lastname >> ','cyan'))
          reg_password=input(colored('\tEnter password >> ','cyan'))
          new_acc=create_account(reg_user_name,reg_f_name,reg_l_name,reg_password)
          save_account(new_acc)
          print("\n\t\tRegistering ...")
          time.sleep(1.5)
          cprint("\n\t\tCONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED","green",attrs=['bold'])
          cprint("\n\tSign into your new account","blue")
          sign_username=input(colored('\n\tEnter username >> ','cyan'))
          sign_password=input(colored('\n\tEnter password >> ','cyan'))
          print("\n\t\tSigning in ...")
          time.sleep(1.5)
          if auth_user(sign_username,sign_password):
            cprint("\n\t\tLOGIN SUCCESSFUL","green",attrs=['bold'])
            sign_name=sign_username
            login=True
          else :
            cprint('\n\t\tSORRY COULD NOT VERIFY USER','red',attrs=['bold'])  
        else:
          cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES','red',attrs=['bold'])  
      elif s_code=='xx':
        cprint(f"""\n\t\tTHANK YOU FOR USING PASSWORD LOCKER
        \t\tBye...
        \t\t\t\t\tClosing App >>>>>
        ""","red",attrs=['bold'])
        time.sleep(1.5)
        logged=False
        break
      else:
        cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES','red',attrs=['bold'])  

    
    while  login==True:
      time.sleep(1.5)
      cprint(f"""
        {sign_name.upper()}, WELCOME TO YOUR PASSWORD LOCKER:
        Use the following commands to navigate the application:
          'sc' >> Save existing page credentials
          'cc' >> Create new page credentials
          'dc' >> Display all credentials saved
          'fc' >> Find credential saved by page name
          'dl' >> Delete page credential
          'lgo' >> Log out
          'ex' >> Close App
          ""","blue")
      app_code=input(colored('\tWhat would you like to do? >> ','cyan')).lower()

      if app_code=='sc':
        cprint('\tEnter pagename,username and password to save credentials >>>\n','blue')
        page_name=input(colored('\n\tEnter pagename >> ','cyan')).lower()
        user_name=input(colored('\n\tEnter page username >> ','cyan'))
        pass_word=input(colored('\n\tEnter page password >> ','cyan'))
        print("\n\t\tSaving credentials ...")
        time.sleep(1.5)
        if check_credential_exists(page_name):
          cprint('\n\t\tCREDENTIALS FOR '+page_name.upper()+' ALREADY EXISTS','red',attrs=['bold'])
        else:    
          new_credential=create_credential(page_name,user_name,pass_word)
          save_credential(new_credential)
          cprint("\n\t\t"+page_name.upper()+", CREDENTIALS SAVED","green",attrs=['bold'])

      elif app_code=='cc':
        cprint('\tEnter pagename,username and password to create and save new page credentials >>>\n','blue')
        page_name=input(colored('\n\tEnter pagename >> ','cyan')).lower()
        user_name=input(colored('\n\tEnter page username >> ','cyan'))
        gen_pass_code=input(colored('\tWould you like to generate a random password? Y/N >> ','cyan')).upper()
        pass_word=''
        if gen_pass_code=='Y':
          pass_word=generate_password()
        else:    
          pass_word=input(colored('\n\tEnter page password >> ','cyan'))
        print("\n\t\tCreating and Saving credentials ...")
        time.sleep(1.5)
        if check_credential_exists(page_name):
          cprint('\n\t\tCREDENTIALS FOR '+page_name.upper()+' ALREADY EXISTS','red',attrs=['bold'])
        else:    
          new_credential=create_credential(page_name,user_name,pass_word)
          save_credential(new_credential)
          cprint("\n\t\t"+page_name.upper()+", CREDENTIALS SAVED","green",attrs=['bold'])

      elif app_code=='dc':
        if len(display_credentials())>0:
          cprint("\n\t\t"+sign_name.upper()+", CREDENTIALS","green",attrs=['bold'])
          for credential in display_credentials():
            cprint(f'''
                -------------------------------------------------------
                    Page Name >>>> {credential.page_name.upper()}               
                    Page Username >>>> {credential.user_name}               
                    Page Password >>>> {credential.pass_word}               
                -------------------------------------------------------
            ''','green')
        else:
          cprint("\n\t\t"+sign_name.upper()+",HAS NO CREDENTIALS SAVED","green",attrs=['bold']) 


      elif app_code=='fc':
        search_page=input(colored('\n\tEnter page name to search credentials >> ','cyan')).lower()
        print("\n\t\tLoading ...")
        time.sleep(1.5)
        if check_credential_exists(search_page):
          found_credential=find_cred_by_pagename(search_page)
          cprint(f'''
                -------------------------------------------------------
                    Page Name >>>> {found_credential.page_name.upper()}               
                    Page Username >>>> {found_credential.user_name}               
                    Page Password >>>> {found_credential.pass_word}               
                -------------------------------------------------------
            ''','green')
        else:
          cprint(f'\n\t\t{search_page.upper()} DOES NOT EXISTS','red',attrs=['bold'])  

      elif app_code=='dl':
        del_page=input(colored('\n\tEnter page name you want to delete >> ','cyan')).lower()
        print("\n\t\tDeleting ...")
        time.sleep(1.5)
        if check_credential_exists(del_page):
          found_page=find_cred_by_pagename(del_page)
          found_page.delete_credential()
          cprint("\n\t\t"+del_page.upper()+", CREDENTIALS DELETED","green",attrs=['bold'])
        else:
          cprint(f'\n\t\t{del_page.upper()} DOES NOT EXISTS','red',attrs=['bold'])

      elif app_code=='lgo':
        cprint(f"""\n\t\t{sign_name.upper()}, THANK YOU FOR USING PASSWORD LOCKER
        \t\tBye...
        \t\t\t\t\tLogin out >>>>>
        ""","green",attrs=['bold'])
        time.sleep(1.5)
        login=False
      elif app_code=='ex':
        cprint(f"""\n\t\t{sign_name.upper()}, THANK YOU FOR USING PASSWORD LOCKER
        \t\tBye...
        \t\t\t\t\tClosing App >>>>>
        ""","red",attrs=['bold'])
        time.sleep(1.5)
        login=False
        logged=False  
      else:
        cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES','red',attrs=['bold'])                         




if __name__ == '__main__':

    main()    




