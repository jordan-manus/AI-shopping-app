import uuid
from typing import Optional
from pydantic import BaseModel, Field


class Users(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    password: str = Field(...)
    email: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    address: str = Field(...)
    phone_number: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "username": "panini_smith",
                "password": "badpassword",
                "email": "panini@email.com",
                "first_name": "panini",
                "last_name": "smith",
                "address": "123 panini lane raleigh, nc",
                "phone_number": "919-867-5309"
            }
        }


class UsersUpdate(BaseModel):
    password: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


    class Config:
        schema_extra = {
            "example": {
                "password": "badpassword",
                "email": "panini@email.com",
                "first_name": "panini",
                "last_name": "weenie",
                "address": "231 panini street raleigh, nc",
                "phone_number": "919-867-5309"
            }
        }