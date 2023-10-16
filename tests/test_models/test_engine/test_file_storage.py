#!/usr/bin/python3
"""
    Test FileStorage
"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Test class for FileStorage class """

    def setUp(self):
        """ Set up new instance of FileStorage """
        self.bm = BaseModel()
        if os.path.exists("file.json"):
            os.rename("file.json", "file.json.old")

    def tearDown(self):
        """ Do clean up """
        del self.bm
        if os.path.exists("file.json.old"):
            os.rename("file.json.old", "file.json")
        FileStorage._FileStorage__objects = {}

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(models.storage, FileStorage)

    def test___file_path(self):
        """ Test __file_path """
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test___objects(self):
        """ Test __objects """
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_new_and_all(self):
        """ Test new() and all() """
        models.storage.new(self.bm)
        models.storage.save()
        models.storage.reload()
        all_objs = models.storage.all()

        self.assertEqual(len(all_objs), 1)
        self.assertIn(f"BaseModel.{self.bm.id}", all_objs)

    def test_save(self):
        """ Test save() """
        self.bm.first_name = "My_name"
        self.bm.save()

        with open("file.json", 'r', encoding="utf-8") as f:
            json_f = f.read()
        self.assertTrue(len(json_f) != 0)
        self.assertIn(f"BaseModel.{self.bm.id}", json_f)

    def test_reload(self):
        """ Test reload() """
        models.storage.reload()
        self.assertIn(
            self.bm.__class__.__name__ + '.' + self.bm.id,
            models.storage.all()
        )

    def test_wrong_input(self):
        """ Test wrong input """
        with self.assertRaises(AttributeError):
            models.storage.new(None)
        with self.assertRaises(AttributeError):
            models.storage.new("example")
