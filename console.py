#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

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
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

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
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name
        """
        if not arg:
            print([str(obj) for obj in storage.all().values()])
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
        print([str(obj)
              for obj in storage.all().values() if type(obj).__name__ == arg])

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
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) == 3:
            print("** attribute name missing **")
            return
        elif len(args) == 4:
            print("** value missing **")
            return
        else:
            obj = storage.all()[key]
            if '{' in arg and '}' in arg:
                import ast
                attr_dict = ast.literal_eval(' '.join(args[2:]))
                if isinstance(attr_dict, dict):
                    for attr_name, attr_value in attr_dict.items():
                        if hasattr(obj, attr_name):
                            attr_type = type(getattr(obj, attr_name))
                            setattr(obj, attr_name, attr_type(attr_value))
                        else:
                            setattr(obj, attr_name, attr_value)
                else:
                    print("** invalid dictionary **")
                    return
            else:
                attr_name = args[2]
                attr_value = args[3].strip('"')
                if hasattr(obj, attr_name):
                    attr_type = type(getattr(obj, attr_name))
                    setattr(obj, attr_name, attr_type(attr_value))
                else:
                    setattr(obj, attr_name, attr_value)
            obj.save()

    def do_count(self, arg):
        """
            Retrieve the number of instances of a class
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in storage.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in storage.all().values()
                    if type(obj).__name__ == arg)
        print(count)

    def default(self, line):
        """Default method to handle custom commands"""
        args = line.split('.')
        if len(args) >= 2:
            class_name = args[0]
            command = args[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                self.do_count(class_name)
            elif command.startswith("show"):
                id = command[5:-1].strip('"')
                self.do_show(f"{class_name} {id}")
            elif command.startswith("destroy"):
                id = command[8:-1].strip('"')
                self.do_destroy(f"{class_name} {id}")
            elif command.startswith("update"):
                args = command[7:-1].split(', ')
                if len(args) == 2:
                    id = args[0].strip('"')
                    dict_rep = eval(args[1])
                    self.do_update(f"{class_name} {id} {dict_rep}")
                elif len(args) == 3:
                    id = args[0].strip('"')
                    attr_name = args[1].strip('"')
                    attr_value = args[2].strip('"')
                    self.do_update(
                        f"{class_name} {id} {attr_name} {attr_value}")
        else:
            super().default(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
