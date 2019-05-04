import os
import re
from typing import Union
from werkzeug.datastructures import FileStorage

from flask_uploads import UploadSet, IMAGES

# set name and allowed extension
IMAGE_SET = UploadSet("images", IMAGES)

def save_image(image: FileStorage, folder: str = None, name: str = None) -> str:
	# takes file storage and saves it to a folder
	return IMAGE_SET.save(image, folder, name)

def get_path(filename: str = None, folder: str = None) -> str:
	# takes image naem and return full path
	return IMAGE_SET.path(filename, folder)

def find_image_any_format(filename: str, folder: str) -> Union[str, None]:
	# takes a filename and returns an image on any of the accepted formats
	for _format in IMAGES:

		image = f"{filename}.{_format}"
		image_path = get_path(image, folder)

		if os.path.isfile(image_path):
			return image_path

	return None

def retrieve_filename(file: Union[str, FileStorage]) -> str:
	# take file storage and return file name
	if isinstance(file, FileStorage):
		return file.filename

	return file

def is_filename_safe(file: Union[str, FileStorage]) -> bool:
	# check regex and return string matches or not
	filename = retrieve_filename(file)

	allowed_format = "|".join(IMAGES)
	regex = f"^[a-zA-Z0-9][a-zA-Z0-9_()-\.]*\.({allowed_format})$"

	return re.match(regex, filename) is not None

def get_basename(file: Union[str, FileStorage]) -> str:
	# return image name in path
	filename = retrieve_filename(file)
	return os.path.split(filename)[1]

def get_extension(file: Union[str, FileStorage]) -> str:
	# return file extension in path
	filename = retrieve_filename(file)
	return os.path.splitext(filename)[1]
