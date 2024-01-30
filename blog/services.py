import smtplib
from email.mime.text import MIMEText

from django.core.mail import send_mail


def send_greet_email(to, subject):
    send_mail(
        "Поздравляем!"
        f""

    )
    # msg = MIMEText(subject, 'plain', 'utf-8')
    # msg['From'] = '<EMAIL>'
    # msg['To'] = '<EMAIL>'
    # msg['Subject'] = subject
    # server = smtplib.SMTP('smtp.gmail')
    # server.starttls()
    # server.login('')
    # server.sendmail('')



