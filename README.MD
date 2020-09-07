# PASSWORD LOCKER
### 04.09.2020
####  A Python program helps you store your credentials for multiple account pages and also generate new credentials for new accounts.
![alt text](images/app1.jpg)
![alt text](images/app2.jpg)

## Author
[Dennis Kamunya](https://github.com/D-Kamunya)

## Versioning
Password Locker V1.0

## Description
A simple python program which runs on the terminal. The app, securely stores your user's account credentials for various pages and also generates passwords for a user's new page account using the inbuilt random and string libraries.

## Features
* The program utilizes two classes:- Account/User and Credential.
* The program authenticates accounts to see their credentials.
* Contains docstrings to document methods and functions.
* Contains a test class for all the classes testing each individual method in a class.

## User Stories
* A user can create a password locker account with my details, a login username and password.
* A user can store my already existing account credentials in the application.
* A user can create new account credentials in the application.
* A user has the option of putting in a password that he/she want to use for the new credential account.
* A user can view various account credentials and their passwords in the application
* A user can delete credentials account that he/she no longer needs in the application.

## Technologies Used
* Python 3.8.2
* Python libraries used:
    * pyperclip
    * random (inbuilt)
    * time (inbuilt)
    * termcolor
    * unittest

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries using pip:
    * **`pip3 install pyperclip`**
    * **`pip3 install termcolor`**
    * **`pip3 install unittest`**

## Setup/Installation
First make sure you have installed the required modules from above as well as have python 3.+ installed in your computer.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`https://github.com/D-Kamunya/Password-Locker.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Open the terminal, go to the project directory and run the following commands: **`chmod +x run.py`** and **`./run.py`** respectively to launch the program.


## Short-codes and Keywords
* Short-codes:
    * **ln**: Logs the user into the locker
    * **xx/ex**: Closes the application
    * **sc**: Save existing page credentials
    * **cc**:Create new page credentials
    * **dc**: Display all credentials saved
    * **fc**: Find credential saved by page name
    * **cp**: Copy pagename credential password to clipboard
    * **dl**:Delete page credential
    * **lgo**: Log out

## Known Bugs
* No known bugs
Be sure to report more bugs by contacting me.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Support and contact details
If you run into any problems feel free to contact me @dennismuriithik@gmail.com

#### License
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2020 Dennis Kamunya


