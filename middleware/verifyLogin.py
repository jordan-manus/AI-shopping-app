#import jwt
from flask_jwt_extended import JWTManager
import secrets
#import User model
#import bycrypt


app.config["JWT_SECRET_KEY"] = secrets.SystemRandom.getrandbits(128)
jwt = JWTManager(app)


def verifyCredentials():
    username = 