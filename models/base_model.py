#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

"""
Class BaseModel that defines all basic attributes for other classes
"""


class BaseModel:

	def __init__(self, *args, **kwargs):
		"""
		Public instance attributes
		datetime to give current date and time
		uuid for a unique id
		"""
		if kwargs:
			"""
			Changing from dictionary to object
			"""
			for key, value in kwargs.items():
				if key == '__class__':
					continue
				if key == 'created_at' or key == 'updated_at':
					value = datetime.fromisoformat(value)
				setattr(self, key, value)
			
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)

	def __str__(self):
		"""
		#__str__ to print readable objects instance
		#__dict__ - a dictionary contains all attributes of an object
		"""
		return f'{[self.__class__.__name__]} ({self.id}) {self.__dict__}'

	def save(self):
		"""
		This method saves an instance of the class
		"""
		self.updated_at = datetime.now()
		storage.save()

	def to_dict(self):
		"""
		Returns a dictionary with attributes of the instance together with a
		a key __class__ with a value of the class name.
		Created_at with ISO format
		"""
		myDict = self.__dict__
		myDict['__class__'] = self.__class__.__name__
		myDict['created_at'] = self.created_at.isoformat()
		myDict['updated_at'] = self.updated_at.isoformat()

		return myDict