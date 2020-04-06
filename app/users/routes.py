from .resources.user import (
    UserRegister,
    UserLogin,
    UserConfirm,
    UserLogout
)

def initialize_routes(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserConfirm, '/confirm/<string:hash_val>')
    api.add_resource(UserLogout, '/logout')