#!/usr/bin/python3
"""test for db storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.state import State
from models.engine.db_storage import DBStorage

try:
    usr = os.getenv('HBNB_MYSQL_USER')
    pwd = os.getenv('HBNB_MYSQL_PWD')
    host = os.getenv('HBNB_MYSQL_HOST')
    db = os.getenv('HBNB_MYSQL_DB')
except:
    pass

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "DB not supported")
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    def setUp(self):
        """set up for test"""
        self.storage = DBStorage()
        self.storage.reload()

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """test if all works in DBStorage"""
        self.objs = self.storage.all()
        self.assertIsNotNone(self.objs)
        self.assertEqual(type(self.objs), dict)

    def test_new(self):
        """Test that a new object is added to the DB"""
        state1 = State()
        setattr(state1, 'name', 'California')
        state2 = State()
        setattr(state2, 'name', 'Arizona')
        state1.save()
        state2.save()
        session = self.storage._DBStorage__session
        self.assertIsNotNone(session)
        results = session.query(State).all()
        self.assertIs(type(results), list)
        """TODO
        Assess results
        """

    def tearDown(self):
        del self.storage

if __name__ == "__main__":
    unittest.main()
