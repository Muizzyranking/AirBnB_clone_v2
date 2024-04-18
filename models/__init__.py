#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
    Checks the environment variable HBNB_TYPE_STORAGE
    uses db storage if the value is db
    otherwise uses file storage

"""
from os import getenv

env = getenv('HBNB_TYPE_STORAGE')

if env == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
