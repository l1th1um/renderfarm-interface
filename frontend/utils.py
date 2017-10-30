import random
import re
import sendgrid
import os
from sendgrid.helpers.mail import *
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASE_DIR, '.env'))

def generate_username(name):
    number = '{:03d}'.format(random.randrange(1, 999))

    name = name.strip()
    #name contain at least firstname and lastname
    if " " in name:
        first_letter = name[0][0].lower()

        #Get Last name
        reg_last_name = r"\s(\w+)$"
        last_name_search = re.search(reg_last_name, name)

        last_name = last_name_search.group().strip().lower()

        username = (first_letter + last_name + number)
    else :
        #Only firstname
        username = (name.strip().lower() + number)

    return username


def send_mail(to_email, subject, content, mode="text/plain"):
    sg = sendgrid.SendGridAPIClient(apikey=os.getenv('SENDGRID_API_KEY'))
    from_email = Email(os.getenv('EMAIL_FROM'))
    to_email = Email(to_email)
    subject = subject
    content = Content(mode, content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())

    return response.status_code