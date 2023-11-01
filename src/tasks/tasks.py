import smtplib
from email.message import EmailMessage

from celery import Celery
from src.config import SMTP_USER, SMTP_PASS

SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379/0')


def get_email_template_dashboard(username: str, user_email: str):
    email = EmailMessage()
    email['Subject'] = 'tradeapp'
    email['From'] = SMTP_USER
    email['To'] = user_email

    email.set_content(
        '<div>'
        f'<h1 style="color: red:">ky, {username}'
        '</div>',
        subtype='html',
    )
    return email


@celery.task
def send_email_report(username: str, user_email: str):
    email = get_email_template_dashboard(username, user_email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
