import json
import datetime
import email
import smtplib
import ssl
import yaml

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def main(config_file, name):
    with open(config_file) as config:
        config_data = yaml.load(config, Loader=yaml.FullLoader)

    today = datetime.datetime.today().strftime("%B %d, %Y")    
    subject = f"{name}'s Classwork for " + str(today)
    body = ""
    sender = config_data['sender']
    sender_password = config_data['sender_password']
    receiver = config_data['receiver']
    
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    
    with open('email.html') as text:
        html = text.read()
    
    mime_html = MIMEText(html, "html")
    message.attach(mime_html)
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, sender_password)
        server.sendmail(sender, receiver, message.as_string())
        
if __name__ == '__main__':
    main()