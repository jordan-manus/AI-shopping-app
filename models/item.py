from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    sale = db.Column(db.Boolean)
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"), unique=False, nullable=False)
    store = db.relationship("SellersModel", back_populates="items")