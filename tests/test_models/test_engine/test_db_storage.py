#!/usr/bin/python3
""" Module for testing db storage"""

import json
import os
import pep8
import unittest
import inspect
import models
from datetime import datetime
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorage(unittest.TestCase):
    """class to test DBStorage methods"""

    def test_pep8(self):
        """tests if DBStorage passes pycodestyle"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docstrings(self):
        """Test docstrings"""
        self.assertIsNotNone(DBStorage.__doc__)

    def test_docs(self):
        """Test documentation"""
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertTrue(DBStorage.all.__doc__)
        self.assertTrue(DBStorage.new.__doc__)
        self.assertTrue(DBStorage.save.__doc__)
        self.assertTrue(DBStorage.reload.__doc__)

    def test_instances(self):
        """chequeamos instantation"""
        obj = DBStorage()
        self.assertIsInstance(obj, DBStorage)

    def test_file_storage_file_path(self):
        """FileStorage __file_path attribute exists"""
        storage = DBStorage()
        self.assertIsNotNone(storage._DBStorage__file_path)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)


if __name__ == '__main__':
    unittest.main()
