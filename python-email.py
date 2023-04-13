# -*- coding: utf-8 -*-
import pickle
import os
from email.message import EmailMessage
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
import pandas as pd
import time
import base64

SCOPES = ['https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.readonly', 
          'https://www.googleapis.com/auth/gmail.send',
          'https://www.googleapis.com/auth/gmail.compose']


def create_message(sender, to, subject, name, cc):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = to
    message["Cc"] = cc
    message["Subject"] = subject
    style = """
            .front {
                font-size: 18px;
                background: azure;
                padding: 20px;
                border-radius: 25px;
            }
    """
    message.set_content(f'''
    <!DOCTYPE html>
    <html>
        <head>
            <style>
            {style}
            </style>
        </head>
        <body>
            <main>
                <div class="front">
                    <p>
                        Dear {name},
                    </p>
                    <p>
                        Hey, how's it going? Today we're going to program an email sending app using Python, Gmail API, EmailMessage and Pandas. And we will write our email in HTML, this allows us to style it using CSS!
                    </p>
                    <ul>
                        <li>
                            List item 1
                        </li>
                        <li>
                            List item 2
                        </li>
                        <li>
                            List item 3
                        </li>
                    </ul>
                    <p>
                        Kind regards,<br>
                        YOUR NAME
                    </p>
                </div>
            </main>
        </body>
    </html>
    ''', subtype='html')

    # Base 64 encode
    b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
    b64_string = b64_bytes.decode()
    return {'raw': b64_string}

def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print( 'Message Id: %s' % message['id'] )
    except HttpError as error:
        print(F'An error occurred: {error}')
        message = False
    return message

def main():
    
    creds = None

    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time. First, it's checked if this already exists.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, attempt to refresh, 
    # otherwise, let the user log in, and then store the credentials.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Load email list and get names and emails
    email_list = pd.read_csv(r"C:\Users\User\Development\email-list.csv") # Change absolute path to where your data file is.
    names = email_list['Name'] # Be sure to check the exact name of fields in the data file (case sensitive)
    emails = email_list['Email']

    # Your email and fixed paramters
    your_email = "FirstName LastName <email@email.com>"
    cc = "" # Leave empty string if no cc
    draft_subject = "Subject Matter"

    success = 0 # Counts the number of successes which will be reported at the end of program execution. 

    # Loop over list of emails and send to each
    for i in range(len(emails)):

        name = names[i]
        email = emails[i]

        # Compose message
        subject = f"To {name} - " + draft_subject
        msg = create_message(your_email, email, subject, name, cc)
        print(f"Attempting to send Email no.{i + 1} to {name} at {email}...")
        response = send_message( service, 'me', msg)
        if response:
            success += 1
        time.sleep(0.1) # Slight delay to not overload the server.
    
    print(f"Email sending done. Successful attempts: {success} out of {len(emails)}")


if __name__ == "__main__":
    main()
