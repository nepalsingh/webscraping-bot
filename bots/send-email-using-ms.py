import smtplib
import os

# ueaaxlpfevpufafx

os.environ['EMAIL'] = 'nepal_singh@hotmail.com'
os.environ['PASSWORD'] = 'statement'
os.environ['RECEIVER'] = 'nepal.singh@gmail.com'

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
receiver = os.environ.get('RECEIVER')

message = """\
Subject: Hi there

This message is sent from Python."""

with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver, message)

