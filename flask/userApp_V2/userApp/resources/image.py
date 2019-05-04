from flask_restful import Resource
from flask_uploads import UploadNotAllowed
from flask import request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
import traceback
import os

from libs import image_helper
from schemas.image import ImageSchema

image_schema = ImageSchema()

class ImageUpload(Resource):

	@jwt_required
	def post(self):

		# retrieve user info from jwt and then saves image to user's folder

		data = image_schema.load(request.files)
		
		# getting user info
		user_id = get_jwt_identity()

		# creating folder name
		folder = f"user_{user_id}"

		try:
			image_path = image_helper.save_image(data["image"], folder=folder)
			basename = image_helper.get_basename(image_path)

			return {"message": "Image '{}' uploaded successfully".format(basename)}, 201

		except UploadNotAllowed:
			extension = image_helper.get_extension(data["image"])
			return {"message": "Extension '{}' not allowed".format(extension)}, 400


class Image(Resource):

	@jwt_required
	def get(self, filename: str):

		# returns requested image if it exists. Looks up inside the logged in user's folder.

		user_id = get_jwt_identity()
		folder = f"user_{user_id}"

		if not image_helper.is_filename_safe(filename):
			return {"message": "File name '{}' not allowed".format(filename)}, 400

		try:
			return send_file(image_helper.get_path(filename, folder=folder))

		except FileNotFoundError:
			return {"message": "'{}' image not found".format(filename)}, 404

	@jwt_required
	def delete(self, filename: str):

		user_id = get_jwt_identity()
		folder = f"user_{user_id}"

		if not image_helper.is_filename_safe(filename):
			return {"message": "File name '{}' not allowed".format(filename)}, 400

		try:
			os.remove(image_helper.get_path(filename, folder=folder))
			return {"message": "Image '{}' deleted".format(filename)}, 200
		except FileNotFoundError:
			return {"message": "Image '{}' not found".format(filename)}, 404
		except:
			traceback.print_exc()
			return {"message": "Could not delete file"}, 500


class AvatarUpload(Resource):

	@jwt_required
	def put(self):

		data = image_schema.load(request.files)
		filename = f"user_{get_jwt_identity()}"
		folder = "avatars"

		avatar_path = image_helper.find_image_any_format(filename, folder)

		if avatar_path:
			try:
				os.remove(avatar_path)
			except:
				return {"message": "Avatar Delete failed"}, 500

		try:
			ext = image_helper.get_extension(data["image"].filename)
			avatar = filename + ext
			avatar_path = image_helper.save_image(
				data["image"], folder=folder, name=avatar
			)
			basename = image_helper.get_basename(avatar_path)
			return {"message": "Avatar Uploaded successfully"}, 200

		except UploadNotAllowed:
			extension = image_helper.get_extension(data["image"])
			return {"message": "Extension '{}' not allowed".format(extension)}, 400