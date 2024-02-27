from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import UsersModel
from db import db
from sqlalchemy.exc import SQLAlchemyError
from schema import UsersSchema

blp = Blueprint("login", "login", description="Logs user in")

@blp.route("/login")
# @app.post('/login')
@blp.arguments(UsersSchema)
@blp.response(201, UsersSchema)
def post(user_data):
    user = UsersModel.query.filter(
            UsersModel.username == user_data["username"]
        ).first()

    # if user and pbkdf2_sha256.verify(user_data["password"], user.password):
    #     access_token = create_access_token(identity=user.id, fresh=True)
    #     refresh_token = create_refresh_token(user.id)
    #     return {"access_token": access_token, "refresh_token": refresh_token}, 200

    if user_data["password"] != user.password:
        abort(401, message="Invalid credentials.")
    else:
        return {"message": "successful sign in"}