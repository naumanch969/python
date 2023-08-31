

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'naumanch969@gmail.com'
email_password = 'cdabkuwdjifekpxy'

email_receiver = 'jebikij365@fulwark.com'

subject = "mail sender python app"
body = """this is the body of the email to be sent from the python email sender app."""
msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['subject'] = subject
msg.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,msg.as_string())

