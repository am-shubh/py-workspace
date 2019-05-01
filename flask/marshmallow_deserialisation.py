from marshmallow import fields, Schema, INCLUDE, EXCLUDE

# when 'INCLUDE' and 'EXCLUDE' is not imported 
# class MobileSchema(Schema):
# 	brand = fields.Str(required=True)
# 	color = fields.Str(required=True)
# 	price = fields.Float(required=True)
# 	description = fields.Str()

# when 'INCLUDE' and 'EXCLUDE' is imported 
class MobileSchema(Schema):
	brand = fields.Str()
	color = fields.Str()
	price = fields.Float()


class Mobile:
	def __init__(self, brand, color, price):
		self.brand = brand
		self.color = color
		self.price = price
	

mobile_data = {
	"brand": "samsung",
	"color": "black",
	"price": 14000.00,
	"description": 'Cool Mobile'
}

mobile_schema = MobileSchema(unknown=EXCLUDE)
mobile = mobile_schema.load(mobile_data)

mobile_obj = Mobile(**mobile)

print(mobile_obj)
