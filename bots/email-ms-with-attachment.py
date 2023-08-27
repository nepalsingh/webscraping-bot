import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


os.environ['EMAIL'] = 'nepal_singh@hotmail.com'
os.environ['RECEIVER'] = 'nepal.singh@gmail.com'

email = os.environ.get('EMAIL')
password = os.environ.get('MSPASSWORD')
receiver = os.environ.get('RECEIVER')

message = MIMEMultipart("alternative")
message["Subject"] = "multipart test"
message["From"] = email
message["To"] = receiver

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
this is a test email
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <strong>this is a test email</strong><br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

MIMEText(html, 'html')
message.attach(MIMEText(html, 'html'))


with smtplib.SMTP("smtp.office365.com", 587) as server:
    server.starttls()
    server.login(email, password)
    server.sendmail(email, receiver, message.as_string())
