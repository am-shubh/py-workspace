from typing import Dict, List
from db import db

class ItemModel(db.Model):

	__tablename__ = 'items'

	_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	price = db.Column(db.Float(precision=2))

	store_id = db.Column(db.Integer, db.ForeignKey('stores._id'))
	store = db.relationship('StoreModel')

	def __init__(self, _id: int, name: str, price: float, store_id: int):

		self._id = _id
		self.name = name
		self.price = price
		self.store_id = store_id


	def json(self) -> Dict:

		return {
			'_id': self._id,
			'name': self.name,
			'price': self.price,
			'store_id': self.store_id
		}


	@classmethod
	def findItem(cls, **kwargs) -> "ItemModel":

		for key, value in kwargs.items():
			item = key
			itemValue = value

		if(item == '_id'):
			return cls.query.filter_by(_id=itemValue).first()
		else:
			return cls.query.filter_by(name=itemValue).first()

	def save_to_db(self) -> None:

		db.session.add(self)
		db.session.commit()

	def delete_from_db(self) -> None:

		db.session.delete(self)
		db.session.commit()