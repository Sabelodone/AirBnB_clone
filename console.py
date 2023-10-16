#!/usr/bin/python3
"""Interpreter module"""

import cmd
from models.base_model import BaseModel
from models import storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """Class for the command interpreter."""
    prompt = ">>>> "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
