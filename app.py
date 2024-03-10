from flask import Flask, request
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from dotenv import dotenv_values
from pymongo import MongoClient

from routes import Users, UsersUpdate

config = dotenv_values(".env")

# app = Flask(__name__)
app = FastAPI()

@app.on_event("startup")
def startup_db():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print('connected to the db')


@app.on_event("shutdown")
def shutdown_db():
    app.mongodb_client.close()


@app.get('/')
def hello():
    return "Hello, World!"
    

# @app.get("/users")

@app.post("/register")
def register(user_data):
    user = jsonable_encoder(user_data)
    new_user = request.app.database["users"].insert_one(user)
    created_user = request.app.database["users"].find_one({"_id": new_user.inserted_id})

    return created_user


@app.get("/user")
def list_users():
    users = list(request.app.database["users"].find(limit=100))
    return users





if __name__ == '__main__':
    app.run()

    
    