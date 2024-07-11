#!/usr/bin/python3

import json
import os

"""
A class responsible for seriolization and deserialization of instance
dictionary to and from JSON file
"""


class FileStorage:
	"""
	Private class attributes
	__file_path - a string path to JSON file(.json)
	__objects - dict that will store all objects by <class name>.id
	"""
	__file_path = 'file.json'
	__objects = {}

	def all(self):
		"""
		Returns the __objects dictionary
		"""
		return self.__objects

	def new(self, obj):
		"""
		sets in __objects dict the obj with key <obj class name>.id
		"""
		name_id = f'{obj.__class__.__name__}.{obj.id}'
		self.__objects[name_id] = obj

	def save(self):
		"""
		Serializes __objects to JSON file(__file_path)
		"""
		with open(self.__file_path, 'w') as f:
			json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

	def reload(self):
		"""
		Deserializes JSON file to __objects only if file exists
		"""
		if os.path.exists(self.__file_path):
			with open(self.__file_path, 'r') as f:
				try:
					obj_dict = json.load(f)
					from models.base_model import BaseModel
					for key, value in obj_dict.items():
						cls_name = value['__class__']
						if cls_name == 'BaseModel':
							"""
							converting from dictionary to object
							"""
							self.__objects[key] = BaseModel(**value)
				except json.JSONDecodeError:
					#handle empty or invalid JSON file case
					pass