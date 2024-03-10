from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, create_refresh_token

from db import db
from models import UsersModel
from schema import UsersSchema


blp = Blueprint("Users", "users", description="Operations on users")


# register endpoint blueprint
@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UsersSchema)
    def post(self, user_data):
        if UsersModel.query.filter(UsersModel.username == user_data["username"]).first():
            abort(409, message="A user with that name already exists")


        user = UsersModel(
            username = user_data["username"],
            password = pbkdf2_sha256(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()


        return {"message": "User created successfully"}, 201



# login endpoint blueprint
@blp.route("/login")
# @blp.response(201, UsersSchema)
class UserLogin(MethodView):
    @blp.arguments(UsersSchema)
    def post(user_data):
        user = UsersModel.query.filter(
                UsersModel.username == user_data["username"]
            ).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}, 200

        if user_data["password"] != user.password:
            abort(401, message="Invalid credentials.")
        else:
            return {"message": "successful sign in"}

    

# endpoint to access individual user by user_id
@blp.route("/user/<int:user_id>")
class Users(MethodView):
    @blp.response(200, UsersSchema)
    def get(self, user_id):
        user = UsersModel.query.get_or_404(user_id)
        return user


    def delete(self, user_id):
        user = UsersModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200