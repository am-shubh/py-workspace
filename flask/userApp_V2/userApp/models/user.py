from requests import Response
from flask import request, url_for
from db import db

from libs.mailgun import Mailgun

class UserModel(db.Model):

	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), nullable=False, unique=True)
	password = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(80), nullable=False, unique=True)
	activated = db.Column(db.Boolean, default=False)

	def save_to_db(self) -> None:
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self) -> None:
		db.session.delete(self)
		db.session.commit()

	def send_confirmation_email(self) -> Response:

		confirmation_link = request.url_root[:-1] + url_for("confirmuser", userId=self.id)
		subject = "Confirm your Registration"
		text = f"Please Click the link to confirm your registration:  {confirmation_link}"
		html = f'<html>Please Click the link to confirm your registration:  <a href="{confirmation_link}">{confirmation_link}</a></html>'

		return Mailgun.send_email([self.email], subject, text, html)
		

	
	@classmethod
	def find_by_email(cls, email: str) -> "UserModel":

		return cls.query.filter_by(email = email).first()

	@classmethod
	def find_by_username(cls, username: str) -> "UserModel":

		return cls.query.filter_by(username = username).first()

	@classmethod
	def find_by_id(cls, _id: int) -> "UserModel":

		return cls.query.filter_by(id = _id).first()


