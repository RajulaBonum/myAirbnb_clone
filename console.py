#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

"""
A python console to automate the CRUD process

"""

class HBNBCommand(cmd.Cmd):
	prompt = ('hbnb ')

	"""
	Quit and EOF to exit
	"""

	def do_quit(self, line):
		"""Quit command to exit the program
		"""
		return True

	def do_EOF(self, line):
		"""
		Exits the command line if ctrl + D is punched
		"""
		print()
		return True

	def emptyline(self):
		"""Do nothing when an emptyline is passed"""
		pass

	def do_create(self, line):
		"""Creates a new instance of BaseModel, saves it (to the JSON file) \
		and prints the id. Ex: $ create BaseModel"""

		if not line:
			print(" ** class name missing **")
		else:
			if line != 'BaseModel':
				print("** class doesn't exist **")
			else:
				new_obj = BaseModel()
				new_obj.save()
				print(new_obj.id)

	def do_show(self, line):
		"""Prints the string representation of \
		 an instance based on the class name and id"""

		args = line.split()

		if not line:
			print("** class name missing **")
		else:
			if args[0] != 'BaseModel':
				print("** class doesn't exist **")
			else:
				if len(args) < 2:
					print("** instance id missing **")
				else:
					name_id = '.'.join(args)
					all_objs = storage.all()
					if name_id not in all_objs.keys():
						print("** no instance found **")
					else:
						print(all_objs[name_id])

	def do_destroy(self, line):
		"""Deletes an instance based on the class name and id (save the change into the JSON file
		). Ex: $ destroy BaseModel 1234-1234-1234."""

		args = line.split()

		if not line:
			print("** class name missing **")
		else:
			if args[0] != 'BaseModel':
				print("** class doesn't exist **")
			else:
				if len(args) < 2:
					print("** instance id missing **")
				else:
					name_id = '.'.join(args)
					all_objs = storage.all()
					if name_id not in all_objs.keys():
						print("** no instance found **")
					else:
						del all_objs[name_id]
						storage.save()

	def do_all(self, line):
		""" Prints all string representation of all instances based 
		or not on the class name. Ex: $ all BaseModel or $ all."""

		all_objs = storage.all()

		if line not in all_objs.keys():
			print("** class doesn't exist **")
			return
		if line:
			print([str(all_objs[key]) for key in all_objs if key.startswith(line)])
		else:
			print([str(all_objs[key]) for key in all_objs])

	def do_update(self, line):
		"""Updates an instance based on the class name and id 
		by adding or updating attribute (save the change into the JSON file). 
		Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""

		args = line.split()

		if not line:
			print("** class name missing **")
		else:
			if args[0] != 'BaseModel':
				print("** class doesn't exist **")
			else:
				if len(args) < 2:
					print("** instance id missing **")
				else:
					name_id = '.'.join(args[:2])
					all_objs = storage.all()
					if name_id not in all_objs.keys():
						print("** no instance found **")
					else:
						if len(args) < 3:
							print("** attribute name missing **")
						else:
							obj = all_objs[name_id]
							attr_name = agrs[2]
							attr_value = args[3].strip('"')

							if hasattr(obj, attr_name):
								attr_name = type(getattr(obj, attr_name))
								attr_value = attr_type(attr_value)
							setattr(obj, attr_name, attr_value)
							obj.save

if __name__ == '__main__':
	HBNBCommand().cmdloop()