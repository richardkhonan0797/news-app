import re

from requests import Response, post
from flask import request, url_for
from flask_mail import Message
from .. import db
from .. import mail

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

MAILGUN_DOMAIN = 'sandboxa9c6f356584d4d9dbc489688bb8daed6.mailgun.org'
MAILGUN_API_KEY = 'a34a430233e317fa9c13c2deab584ff3-46ac6b00-1db2e2a5'
FROM_TITLE = 'News API'
FROM_EMAIL = 'postmaster@sandboxa9c6f356584d4d9dbc489688bb8daed6.mailgun.org'

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), nullable = False, unique = True)
    password = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False, unique = True)
    activated = db.Column(db.Boolean, default = False)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def send_confirmation_email(self):
        link = request.url_root[:-1] + url_for("users.userconfirm", user_id=self.id)
        print(link, 'INI LINK')

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

    def save_to_db(self):
        print('Masuk save')
        db.session.add(self)
        db.session.commit()

    def check(email):
        if(re.search(regex, email)):
            return True
        else:
            return False