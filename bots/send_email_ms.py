import smtplib
import os

def send_email(percent_change):
  os.environ['EMAIL'] = 'nepal_singh@hotmail.com'
  os.environ['RECEIVER'] = 'nepal.singh@gmail.com'

  email = os.environ.get('EMAIL')
  password = os.environ.get('MSPASSWORD')
  receiver = os.environ.get('RECEIVER')

  message = f"""\
  subject: Hi there

  The change is CROBEX more than {percent_change}%."""

  with smtplib.SMTP("smtp.office365.com", 587) as server:
      server.starttls()
      server.login(email, password)
      server.sendmail(email, receiver, message)

