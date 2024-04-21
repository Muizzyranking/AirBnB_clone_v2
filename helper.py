#!/usr/bin/python3
""" Helper Module """
import re


def parser(args):
    """parse the command entered by the user"""
    name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
    class_match = re.match(name_pattern, args)
    obj_kwargs = {}
    if class_match is not None:
        class_name = class_match.group('name')
        params_str = args[len(class_name):].strip()
        params = params_str.split(' ')
        str_pattern = r'(?P<t_str>"([^"]|\")*")'
        float_pattern = r'(?P<t_float>[-+]?\d+\.\d+)'
        int_pattern = r'(?P<t_int>[-+]?\d+)'
        param_pattern = '{}=({}|{}|{})'.format(
            name_pattern,
            str_pattern,
            float_pattern,
            int_pattern
        )
        for param in params:
            param_match = re.fullmatch(param_pattern, param)
            if param_match is not None:
                key_name = param_match.group('name')
                str_v = param_match.group('t_str')
                float_v = param_match.group('t_float')
                int_v = param_match.group('t_int')
                if float_v is not None:
                    obj_kwargs[key_name] = float(float_v)
                if int_v is not None:
                    obj_kwargs[key_name] = int(int_v)
                if str_v is not None:
                    obj_kwargs[key_name] = str_v[1:-1].replace('_', ' ')
    else:
        class_name = args
    return class_name, obj_kwargs


def checker(model, keys, classes, storage):
    """checks if the model string contains any of the specified keys"""

    part = model.split()
    if "n" in keys and not model:
        print("** class name missing **")
        return False
    if "l" in keys and len(model.split()) < 2:
        print("** instance id missing **")
        return False
    if "ec" in keys and part[0] not in classes:
        print("** class doesn't exist **")
        return False
    if "es" in keys and ".".join(part[0:2]) not in storage:
        print("** no instance found **")
        return False
    if "a" in keys and len(model.split()) < 3:
        print("** attribute name missing **")
        return
    if "v" in keys and len(model.split()) < 4:
        print("** value missing **")
        return
    return True
