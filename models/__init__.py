#!/usr/bin/python3
"""This module instantiates an instance of the Storage will be used"""

from os import getenv
from config import HBNB_TYPE_STORAGE

if HBNB_TYPE_STORAGE == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
