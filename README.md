# Python YouEmail
Automated email sending script written in Python using the Gmail API, Pandas and EmailMessage library. Ideal if you have an email you'd like to send to 50+ recipients. Comes with personalized messaging in both the subject and the body of the email. 

## Get Started

_Prerequisites_
- This script requires a Gmail account from which to send the emails. 
- OAuth2 authentication is required as well. See here for guidance: https://developers.google.com/youtube/registering_an_application
- The scopes the script uses are: 'https://mail.google.com/', 'https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/gmail.compose', so make sure those scopes are added this the app's authentication.
```
SCOPES = ['https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.compose']
```
- (TODO after cloning repo) In order to use the OAuth2 with this script, a client_secrets.json file is required that contains information from the API Console. The file should be in the same directory as the script. Once downloaded from the API console, move the .json file into the local script folder (same place as script.py) and rename it so "client_secret.json" - the script will look for a file with this exact name in the local directory.

To setup the python-you-upload project, here are the following guidelines:

* Close the repository ```git clone https://github.com/Firgrep/python-you-email.git```
* Open Project folder on terminal or in your editor (and then open terminal there)
* Prepare your virtual environment ```py -3 -m venv .venv```
* Close terminal and open a new one, virtual environment script should load automatically.
    * If for some reason the virtual environment does not activate, manual activation is possible but it may differ depending on your machine and code editor:
        * On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate
        * On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh
        * On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish
        * On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat
        * On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1
* Install requirements from file ```pip install -r requirements.txt```
* Put the ```client_secrets.json``` from the Google APP Authentication (see above) file in the project directory. Make sure to shorten the filename to the exact one specified. 

Preparing the script for your use
* The script uses Pandas to load a list of names and emails from a .csv file. If you have an excel file or something else, just change the Pandas method ".read_scv" to what's needed. See Pandas documentation https://pandas.pydata.org/docs/
    * Change the path of ```pd.read_csv(r"C:\Users\User\Development\email-list.csv")``` method (line 113) to the location of your .csv file.
    * Double check the fields of your file are "Name" and "Email" (lines 114 and 115), otherwise change the keys in the program to match the data file.

* Set sender email ```your_email = "FirstName LastName <email@email.com>"``` (line 118)
* (Optional) Set Cc email ```cc = "cc@email.org"``` (line 119) 
* Set generic subject ```draft_subject = "Subject Matter"``` (line 120)

* (Optional) Set personalized message. Currently the script is set to add to the subject line "To (name) >>generic subject<<". Edit this as you wish on line 131. If you wish to not use personalized message, you can just turn it into an empty string ("").

* Email body. Starting line 34, the HTML document within the set_content method is the actual body of your message. Tailor it to what you like. Because messages are personalized, an external HTML file has not been used, since the individual (name) is injected into the HTML via Python's f-string. 

* Email style. CSS styling can be used to add extra flourish to your message. Because f-string is used, it was necessary to move this to its own variable, but that might actually be better. Currently a simple background with some padding and border-radius as well as a slightly larger font is in place but feel free to alter these to suit your own needs.

Running the script
* To execute script, put into the terminal ```python python-email.py```
* On first-use, user will be prompted to log into their Gmail to grant the program necessary credentials (this will only work once permissions and authentication file have been prepared, see above re _Prerequisites_) These will then be stored in a .pickle file for future use. 
* Watch Python send your emails like your own private postman!

Testing is recommended on initial use of the script. Make a quick .csv file with an email you have (or your own), and see that everything works and the message outputs as expected (note that styling may vary based on email service; what may appear colored in Gmail, may not in Outlook...)

I hope you find this useful! Please report here on github if you come across any bugs.
