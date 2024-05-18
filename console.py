#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    classes = {
	'BaseModel': BaseModel 
	}

    prompt = '(hbnb) '
    storage_all = storage.all()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()  # To ensure a new line after EOF is entered
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new = storage.get_attr_name_from_classes(arg)
            new_instance = new()
            new_instance.save()
            print(new_instance.id)
        except TypeError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance
            based on the class name and id
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in self.storage_all:
            print("** no instance found **")
            return
        print(self.storage_all[key])

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and
            id (save the change into the JSON file)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in self.storage_all:
            print("** no instance found **")
            return
        del self.storage_all[key]
        storage.save()

    def do_all(self, arg):
<<<<<<< HEAD
        """Prints all string representation of all instances based or not on the class name"""
<<<<<<< HEAD
        args = arg.split()
        if not args:
            print([str(obj) for obj in storage.all()])
            return
            
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        print([str(storage.all()[obj]) for obj in storage.all() if str(obj.split(".")[0]) == args[0]])
        
	#for obj in storage.all():
         #   if obj.split(".")[0] == args[0]:
          #      print(str(storage.all()[obj]))
=======
=======
        """
            Prints all string representation of all instances
            based or not on the class name
        """
>>>>>>> 0d401f66a2122b30544ae94175aabcf852de2469
        if not arg:
            for obj in self.storage_all:
                print([str(self.storage_all[obj])])
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
<<<<<<< HEAD
        print([str(self.storage_all[obj]) for obj in self.storage_all.values() if type(obj).__name__ == arg])
>>>>>>> 1420dafcff68d6ad94816d8ffb067265b0a8195b
=======
        for obj in self.storage_all.values():
            if type(obj).__name__ == arg:
                print([str(self.storage_all[obj])])
>>>>>>> 0d401f66a2122b30544ae94175aabcf852de2469

    def do_update(self, arg):
        """
            Updates an instance based on the class name and
            id by adding or updating attribute
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + '.' + args[1]
        if key not in self.storage_all:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = self.storage_all[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
