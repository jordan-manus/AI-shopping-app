from flask import Flask, redirect, url_for, request, flash, jsonify
from models import UsersModel
from flask_smorest import abort, Api
from db import db

from flask_jwt_extended import JWTManager

from routes.items import blp as ItemBlueprint
from routes.users import blp as UserBlueprint


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

    app.config["JWT_SECRET_KEY"] = "jordan"
    jwt = JWTManager(app)

# checks if user is admin
    @jwt.additional_claims_loader
    def additional_claims_to_jwt(identity):
        # look in DB to verify is user is admin before this block of code
        if identity ==1:
            return {"is_admin": True}
        return {"is_admin": False}
    

    @jwt.expired_token_loader
    def expired_token_loader(jwt_header, jwt_payload):
        return(
            jsonify({"message": "The token has expired", "error": "token_expired"}),
            401,
        ),
        
    @jwt.invalid_token_loader
    def invalid_token_loader(error):
        return (
            jsonify({"message": "Signature verification failed", "error": "invalid_token"}),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify({
                    "description": "Request does not contain an access token.",
                "error": "authorization_required",
            })
        )
    



    with app.app_context():
        db.create_all()

    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

