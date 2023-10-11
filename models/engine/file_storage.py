#!/usr/bin/python3

"""
Module: file_storage.py

Defines a `FileStorage` class.
"""

import os
import json
from models.base_model import BaseModel

class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing.
        """
        current_classes = {
            'BaseModel': BaseModel,
            'User': User,  # Restore User import
            'Amenity': Amenity,  # Restore Amenity import
            'City': City,  # Restore City import
            'State': State,  # Restore State import
            'Place': Place,  # Restore Place import
            'Review': Review,  # Restore Review import
        }

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}