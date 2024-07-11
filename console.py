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
			return

		if line not in globals():
			print("** class doesn't exist **")
			return

		new_instance = globals()[line]()
		new_instance.save()
		print(new_instance.id)

	def do_show(self, line):
		"""Prints the string representation of \
		 an instance based on the class name and id"""

		args = line.split()

		if not line:
			print("** class name missing **")
			return

		if args[0] not in globals():
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		name_id = f'{args[0]}.{args[1]}'
		all_objs = storage.all()

		if name_id not in all_objs.keys():
			print("** no instance found **")
			return

		print(all_objs[name_id])
		
	def do_destroy(self, line):
		"""Deletes an instance based on the class name and id (save the change into the JSON file
		). Ex: $ destroy BaseModel 1234-1234-1234."""

		args = line.split()

		if not line:
			print("** class name missing **")
			return

		if args[0] not in globals():
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		name_id = f'{args[0]}.{args[1]}'
		all_objs = storage.all()

		if name_id not in all_objs.keys():
			print("** no instance found **")
			return

		del all_objs[name_id]
		storage.save()
					
	def do_all(self, line):
		""" Prints all string representation of all instances based 
		or not on the class name. Ex: $ all BaseModel or $ all."""

		if line and line not in globals():
			print("** class doesn't exist")
			return

		all_objs = storage.all()

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
			return

		if args[0] not in globals():
			print("** class doesn't exist **")
			return

		if len(args) < 2:
			print("** instance id missing **")
			return

		name_id = f'{args[0]}.{args[1]}'
		all_objs = storage.all()

		if name_id not in all_objs.keys():
			print("** no instance found **")
			return

		if len(args) < 3:
			print("** attribute name missing **")
			return

		if len(args) < 4:
			print("** Value missing **")
			return

		obj = all_objs[name_id]
		attr_name = agrs[2]
		attr_value = args[3].strip('"')
		if hasattr(obj, attr_name):
			attr_type = type(getattr(obj, attr_name))
			attr_value = attr_type(attr_value)

		setattr(obj, attr_name, attr_value)
		obj.save

if __name__ == '__main__':
	HBNBCommand().cmdloop()