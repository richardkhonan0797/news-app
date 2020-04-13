import re
import hashlib
import random

from requests import Response
from flask import request, url_for
from flask_mail import Message
from .. import db
from .. import mail

from ..helpers.email import sendEmail

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(40), nullable = False, unique = True)
    password = db.Column(db.String(40), nullable = False)
    email = db.Column(db.String(40), nullable = False, unique = True)
    activated = db.Column(db.Boolean, default = False)
    hash_val = db.Column(
        db.String(32), 
        default = hashlib.md5(str(random.randint(1,100)).encode()).hexdigest()
    )

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_hash_val(cls, hash_val):
        return cls.query.filter_by(hash_val=hash_val).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def send_confirmation_email(self):
        link = request.url_root[:-1] + url_for("users.userconfirm", hash_val=self.hash_val)
        return sendEmail(link), 200

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
