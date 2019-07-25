from sys import *
import time
import smtplib
from urllib.request import urlopen
import pandas as pd

def is_connected():
    try:
        urlopen('http://216.58.192.142',timeout=1)
        return True
    except Exception as err:
        return False

def MailSender(gmail_user,gmail_password):
    sent_from = gmail_user
    to = ['atultiware52@gmail.com']

    email_text = "Welcome to Automation Mail Sending..."

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo()
        server.login(gmail_user,gmail_password)
        server.sendmail(sent_from,to,email_text)
        server.close()
        
        print("Mail sent Successfully...")

    except Exception as E:
        print("Unable to send Mail.",E)

def main():
    print("----Automation Email Send----")

    print("Application name :"+argv[0])

    try:
        gmail_user = 'atultiware92@gmail.com'
        gmail_password = '9130455252'

        connected = is_connected()

        if connected:
            startTime = time.time()
            MailSender(gmail_user,gmail_password)
            endTime = time.time()

            print('Took %s seconds to internet connection')
        else:
            print('There is no internet connection')

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()        

