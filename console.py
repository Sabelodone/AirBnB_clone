#!/usr/bin/python3
"""Interpreter module"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self.precmd(line)

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
