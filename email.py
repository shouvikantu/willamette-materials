import imaplib
import email
import os

# Authenticate IMAP credentials
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('sahmed@willamette.edu', 'pass')
mail.select("inbox")
# Create folders for filtered emails
for folder in ['Newsletters', 'Bills', 'Important']:
    mail.create(folder)
# Filter and move emails
def filter_emails():
    result, data = mail.search(None, "ALL")
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        if 'newsletter' in email_message['subject'].lower():
            mail.copy(num, 'Newsletters')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif 'bill mail.copy(num, 'Bills')
            mail.store(num, '+FLAGS', '\\Deleted')
        elif 'important' in email_message['subject'].lower():
            mail.copy(num, 'Important')
            mail.store(num, '+FLAGS', '\\Deleted')mail.expunge()
# Automatically respond to urgent emails
def respond_to_urgent_emails():
    # code to check email
    for msg in messages:
        if 'urgent' in msg['subject'].lower():
            # send urgent response
            response = 'Thank you for your email. I am currently unavailable, but I will respond as soon as possible.'
            os.system('echo "{}" | mail -s "Urgent Response" "{}"'.format(response, msg['from']))