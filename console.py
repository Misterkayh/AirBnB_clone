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

    def default(self, args):
        """Default action is command is not available"""
        if '.' not in args:
            super().default(args)
            return
        class_name, *others = args.split(".")

        if others[0] == "all()":
            self.do_all(class_name)

        elif others[0] == "count()":
            objs = models.storage.all()
            count = 0
            for key in objs.keys():
                if class_name in key:
                    count += 1
            print(count)

        elif "show(" in others[0] and others[0][-1] == ')':
            show_id = others[0][5:-1]
            show_arg = class_name + ' ' + show_id
            self.do_show(show_arg)

        elif "destroy(" in others[0] and others[0][-1] == ')':
            destroy_id = others[0][8:-1]
            destroy_arg = class_name + ' ' + destroy_id
            self.do_destroy(destroy_arg)

        elif "update(" in others[0] and others[0][-1] == ')':
            up_args = others[0][7:-1]
            up_args = up_args.split(", ")
            for i in range(len(up_args)):
                up_args[i] = up_args[i].strip('"')
            update_arg = class_name
            for val in up_args:
                update_arg += ' ' + val
            self.do_update(update_arg)

        else:
            super().default(args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
