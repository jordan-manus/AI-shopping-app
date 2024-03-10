from db import db


class OrdersModel(db.Model):
    __tablename__ = "orders"

    order_id =db.Column(db.Integer, primary_key=True)
    # item_array = 
    # order_date

    user_id = db.Column(db.Integer, db.ForeignKey("sellers.id"), unique=False, nullable=False)
    orders = db.relationship("UsersModel", back_populates="users")