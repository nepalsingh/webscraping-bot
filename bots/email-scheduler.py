import yagmail
import os
import csv


# ueaaxlpfevpufafx
os.environ['EMAIL'] = 'nepal.singh@gmail.com';
os.environ['PASSWORD'] = 'ueaaxlpfevpufafx';
os.environ['RECEIVER'] = 'jasec4@xidprinting.com'

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')
receiver = os.environ.get('RECEIVER')
yag = yagmail.SMTP(user=email, password=password)

# Email Scheduler
def email_scheduler():
    # Email Scheduler
    yag.send(receiver, "Hello from Yagmail", "Hello, this is a test")

csv_file = 'files/contacts.csv'
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for name, email,amount,filepath in reader:
        print(f'Sending email to {name}, {email}, {amount}, {filepath}')
        content = [f'Hello {name},\n\nThank you for your donation of ${amount}.\n\nIt will be put to very good use.\n\nSincerely,\n\n-Nepal Singh', 'files/{filepath}']
        yag.send(email, content)

#email_scheduler()
