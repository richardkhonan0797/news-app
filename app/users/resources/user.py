from werkzeug.security import safe_str_cmp
from flask_restful import Resource
from flask import (
    request,
    make_response,
    render_template
)
from ...models.user import UserModel
from ...schemas.user import UserSchema
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_raw_jwt
)
from ... import blacklist

user_schema = UserSchema()

NOT_ACTIVATED = 'You have not activated your account, please check your email <{}>.'
INVALID_CREDENTIALS = 'You have invalid credentials.'
USER_NOT_FOUND = 'User not found'
USERNAME_EXISTS = 'A user with that username already exists.'
EMAIL_EXISTS = 'A user with that email already exists.'
CREATED_SUCCESS = 'Account created successfully, a confirmation link has been sent to your email.'
FAILED_TO_CREATE = 'Internal Server Error'


class UserRegister(Resource):
    def post(self):
        user_json = request.get_json()
        print(user_json, "INI USER")
        if UserModel.find_by_username(user_json["username"]):
            return {'message': USERNAME_EXISTS}, 400
        
        if UserModel.find_by_email(user_json["email"]):
            return {'message': EMAIL_EXISTS}, 400

        if UserModel.check(user_json['email']):
            user = user_schema.load(user_json)
            try:
                user.save_to_db()
                user.send_confirmation_email()
                return {'message': CREATED_SUCCESS}, 201
            except:
                return {'message': FAILED_TO_CREATE}, 500
        else:
            return {'message': 'Please input a valid email address.'}

class UserLogin(Resource):
    def post(self):
        user_json = request.get_json()

        user = UserModel.find_by_username(user_json["username"])

        if user and safe_str_cmp(user_json["password"], user.password):
            if user.activated:
                access_token = create_access_token(identity=user.id, fresh=True)
                refresh_token = create_refresh_token(identity=user.id)
                return {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, 200
            else:
                return {'message': NOT_ACTIVATED.format(user.email)}, 400

        return {'message': INVALID_CREDENTIALS}, 401

class UserConfirm(Resource):
    def get(self, hash_val):
        user = UserModel.find_by_hash_val(hash_val)
        
        if user:
            user.activated = True
            user.save_to_db()
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('confirmation_page.html', email=user.email), 200, headers)
        else:
            return {'message': USER_NOT_FOUND}, 404

class UserLogout(Resource):
    @jwt_required
    def delete(self):
        jti = get_raw_jwt()['jti']
        blacklist.add(jti)
        return {'message': 'successfully logged out'}, 200
