#!/usr/bin/python3
"""
    AirBnb Clone Console Entry Point
"""
import cmd
import shlex
import models
from models.engine.file_storage import MY_CLS

MY_INTS = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]
MY_FLOATS = ["latitude", "longitude"]


class HBNBCommand(cmd.Cmd):
    """ AirBnB Clone Console """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit to exit the program\n"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program\n"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line + ENTER is entered"""
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id\n"""
        my_args = shlex.split(args)

        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in MY_CLS.keys():
            print("** class doesn't exist **")
        else:
            my_instance = MY_CLS[my_args[0]]()
            print(my_instance.id)
            my_instance.save()

    def do_show(self, args):
        """Prints the string representation of an
        instance based on the class name and id\n"""
        my_args = shlex.split(args)

        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in MY_CLS.keys():
            print("** class doesn't exist **")
        elif len(my_args) < 2:
            print("** instance id missing **")
        else:
            model_objs = models.storage.all()
            obj_key = my_args[0] + "." + my_args[1]
            if obj_key in model_objs.keys():
                print(model_objs[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        my_args = shlex.split(args)

        if not my_args:
            print("** class name missing **")
        elif my_args[0] not in MY_CLS.keys():
            print("** class doesn't exist **")
        elif len(my_args) < 2:
            print("** instance id missing **")
        else:
            model_objs = models.storage.all()
            obj_key = my_args[0] + "." + my_args[1]
            if obj_key in model_objs.keys():
                del model_objs[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name\n"""
        my_args = shlex.split(args)
        all_objs = []

        if not my_args:
            for key, value in models.storage.all().items():
                all_objs.append(str(value))
        elif my_args[0] in MY_CLS.keys():
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == my_args[0]:
                    all_objs.append(str(value))
        else:
            print("** class doesn't exist **")

        if all_objs:
            print(all_objs)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        Only one attribute can be updated at the time\n"""
        my_args = shlex.split(args)

        if not my_args:
            print("** class name missing **")
            return

        elif my_args[0] not in MY_CLS.keys():
            print("** class doesn't exist **")
            return

        elif len(my_args) == 1:
            print("** instance id missing **")
            return

        elif len(my_args) >= 2:
            obj_key = my_args[0] + "." + my_args[1]
            if obj_key not in models.storage.all().keys():
                print("** no instance found **")
                return
            else:
                if len(my_args) == 2:
                    print("** attribute name missing **")
                    return

        if len(my_args) == 3:
            print("** value missing **")

        if len(my_args) >= 4:
            dict_obj = models.storage.all()
            obj_key = my_args[0] + "." + my_args[1]

            if my_args[2] in MY_INTS:
                my_args[3] = int(my_args[3])
            if my_args[2] in MY_FLOATS:
                my_args[3] = float(my_args[3])

            setattr(dict_obj[obj_key], my_args[2], my_args[3])
            models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
