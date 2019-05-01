from marshmallow import fields, Schema

class MobileSchema(Schema):
	brand = fields.Str()
	color = fields.Str()
	price = fields.Float()

class Mobile:

	def __init__(self, brand, color, price, features):
		self.brand = brand
		self.color = color
		self.price = price
		self.features = features


mobile = Mobile('samsung', 'black', 14000.00, 'Cool Mobile')

mobile_schema = MobileSchema()
mobile_data = mobile_schema.dump(mobile)

print(mobile_data)