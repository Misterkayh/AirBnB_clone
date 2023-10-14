#!/usr/bin/python3
"""
    Test for the BaseModel class
"""
import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test class for BaseModel """

    def setUp(self):
        """ Set up instance of basemodel to this class's instance attritube """
        self.basemodel = BaseModel()

    def tearDown(self):
        """ Clean up """
        del self.basemodel

    def test_instance(self):
        """ Test instance type """
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_id(self):
        """ Test id """
        self.assertIsInstance(self.basemodel.id, str)

    def test_created_at(self):
        """ Test created_at """
        self.assertIsInstance(self.basemodel.created_at, datetime)

    def test_updated_at(self):
        """ Test updated_at """
        self.assertIsInstance(self.basemodel.updated_at, datetime)

    def test_two_different_instances(self):
        """ Test two different instances """
        my_bm = BaseModel()
        self.assertFalse(self.basemodel is my_bm)

    def test_unique_ids(self):
        """ Test unique ids """
        my_bm = BaseModel()
        self.assertTrue(self.basemodel.id != my_bm.id)

    def test___str__(self):
        """ Test string representation of BaseModel """

        str_rep = str(self.basemodel)
        my_str = "[{}] ({}) {}".format(
                                    self.basemodel.__class__.__name__,
                                    self.basemodel.id,
                                    self.basemodel.__dict__)
        self.assertEqual(str_rep, my_str)

    def test_save_and_updated_time(self):
        """ Test save and updated time """
        self.basemodel.save()
        self.assertTrue(self.basemodel.created_at != self.basemodel.updated_at)

    def test_to_dict(self):
        """ Test to_dict() """
        my_dict = self.basemodel.to_dict()
        my_dict_keys = ["id", "created_at", "updated_at", "__class__"]
        for key in my_dict_keys:
            self.assertIn(key, my_dict.keys())

    def test_from_dict_to_instance(self):
        """ Test from dict to instance """
        self.basemodel.new_attribute = "Samir"
        bm_dict = self.basemodel.to_dict()

        new_bm = BaseModel(**bm_dict)
        new_bm_dict = new_bm.to_dict()
        
        for key in bm_dict.keys():
            self.assertEqual(bm_dict[key], new_bm_dict[key])
