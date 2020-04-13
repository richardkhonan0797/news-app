import os

from requests import post

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

MAILGUN_DOMAIN = os.getenv('MAILGUN_DOMAIN')
MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
FROM_TITLE = os.getenv('FROM_TITLE')
FROM_EMAIL = os.getenv('FROM_EMAIL')

def sendEmail(link):
    return post(
            f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
            auth=("api", MAILGUN_API_KEY),
            data={
                "from": f"{FROM_TITLE} <{FROM_EMAIL}>",
                "to": self.email,
                "subject": "Registration confirmation",
                "text": f"Please click the link to confirm your registration: {link}",
            },
        )

def check(email):
    if(re.search(regex, email)):
        return True
    else:
        return False