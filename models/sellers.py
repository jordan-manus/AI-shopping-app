from db import db


class SellersModel(db.Model):
    __tablename__ = "sellers"

    id = db.Column(db.Integer, primary_key=True)
    seller_name = db.Column(db.String(50), unique=True, nullable=True)
    address = db.Column(db.String(100), unique=True, nullable=True)
    phone_number = db.Column(db.String(15))
    email = db.Column(db.String(50), nullable=True)
    items = db.relationship("ItemModel", back_populates="sellers", lazy="dynamic")