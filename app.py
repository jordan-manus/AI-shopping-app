from flask import Flask, redirect, url_for, request, flash
from models import UsersModel
from flask_smorest import abort, Api
from db import db

from routes.login import blp as LoginBlueprint


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Shopping REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(LoginBlueprint)

#     return app


# create_app("postgres://superuser:@127.0.0.1:5432/aiShoppingTool")


# @app.post('/login')
# def login(user_data):
#     user = UsersModel.query.filter(
#             UsersModel.username == user_data["username"]
#         ).first()

#     # if user and pbkdf2_sha256.verify(user_data["password"], user.password):
#     #     access_token = create_access_token(identity=user.id, fresh=True)
#     #     refresh_token = create_refresh_token(user.id)
#     #     return {"access_token": access_token, "refresh_token": refresh_token}, 200

#     if user_data["password"] != user.password:
#         abort(401, message="Invalid credentials.")
#     else:
#         return {"message": "successful sign in"}



# allows the user to register a brand new account
# @app.route('/register', methods=['POST'])
# def register():
#     pass


# # allows the user to create/edit their initial questionnaire 
# @app.route('/questionnaire', methods=['POST', 'PUT'])
# def questionnaire():
#     pass


# # allows the user to create and retrieve items from DB
# @app.route('/items', methods=['POST', 'GET'])
# def items():
#     pass


# if __name__ == '__main__':
#     app.run(debug=True)
