from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    item_name = fields.Str(required=True)
    price = fields.Float(required=True)
    sale = fields.Bool()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainItemSchema(), dump_only=True)


class PlainSellersSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    address = fields.Str()
    phone_number = fields.Str()
    email = fields.Str(required=True)


class SellersSchema(PlainSellersSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class UsersSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    address = fields.Str()
    phone_number = fields.Str()
