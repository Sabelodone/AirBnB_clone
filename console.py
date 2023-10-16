#!/usr/bin/python3
"""Interpreter module"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Interpreter class of the prompt"""
    prompt = "(hbnb) "

    def do_help(self, arg):
        """Display a help message"""
        if arg == "quit":
            print("Quit command to exit the program")
        else:
            super().do_help(arg)

    def do_EOF(self, line):
        """EOF Handler"""
        print()
        return True

    def emptyline(self):
        """No execution performed"""
        pass

    def do_quit(self, arg):
        "Exit th console"
        return True

    def default(self, arg):
        """Get the commands that matches no file instruction"""
        self.precmd(arg)

    def precmd(self, arg):
        return cmd.Cmd.precmd(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
