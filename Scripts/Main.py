import smtplib, ssl
import pandas as pd


smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "lavachoco218@gmail.com"
cpassword = input("Type your password and press enter: ")
#password = 'chocolava@002'
receivers = ['mishraanurag218@live.com']
# Create a secure SSL context
context = ssl.create_default_context()
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

smtp_data = pd.read_csv('./Data/smtp.csv')
mails_data = pd.read_csv('./Data/email.csv')



# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()






