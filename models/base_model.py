#!/usr/bin/python3

import uuid
from datetime import datetime
"""
Module: base.py
"""


class BaseModel:
    """
    Base class which defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes an object with its attributes.
        """
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns the string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        from models import storage '''Import storage only when needed'''
        """
        Updates the public instance attribute,
        updated_at' with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of the instance's __dict__.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()

        return obj_dict
