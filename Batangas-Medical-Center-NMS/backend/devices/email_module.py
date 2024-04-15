import smtplib
from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

if __name__=="__main__":
    subject = "Alert Device"
    body = "This Device is down. here are the details."
    sender = ""
    recipients = ["", ]
    password = "mysy bhty ijhx tcat" #"zogt bmje dmbg vivf"
    # mysy bhty ijhx tcat fifibuy


    send_email(subject, body, sender, recipients, password)
