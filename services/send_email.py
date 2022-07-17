import smtplib
from email.mime.text import MIMEText

from .keys import sender, password


def send_email(name, email, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    message = f'{message}\nMy name is {name} \nMy email {email}'

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = sender
        server.sendmail(sender, sender, msg.as_string())
    except Exception as ex:
        return f'{ex}\nCheck your login or password!'