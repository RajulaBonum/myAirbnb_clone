#!/usr/bin/python3

"""class BaseModel that defines all common attributes/methods
 for other classes
 """

 import uuid # For generatin an id for class
 from datetime import datetime

 class BaseModel:

 	def __init__(self, id, created_at, updated_at):
 	"""
 	Public instance attributes
 	datetime class to give the current date and time
 	uuid to give the instance a unique id
 	"""
 	self.id = uuid.uuid4()
 	self.created_at = datetime.now()
 	self.updated_at = datetime.now()

 	#__str__ to print readable objects instances
 	#__dict__ - a dictionary contains all attributes of an object
 	def __str__(self):
 		print(f'{[self.__class__.__name__]} {<self.id>} {<self.__dict__>}')

 	def save(self):
 		"""
 		This method saves an instance of the class
 		"""
 		self.updated_at = datetime.now()

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



