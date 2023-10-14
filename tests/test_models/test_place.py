#!/usr/bin/python3
"""
    Test class Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test class for class Place """

    def setUp(self):
        """ Set up a new place instance """
        self.plc = Place()

    def tearDown(self):
        """ Clean up """
        del self.plc

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.plc, Place)

    def test_city_id(self):
        """ Test city id """
        self.assertIsInstance(self.plc.city_id, str)

    def test_user_id(self):
        """ Test user id """
        self.assertIsInstance(self.plc.user_id, str)

    def test_name(self):
        """ Test place name """
        self.assertIsInstance(self.plc.name, str)

    def test_description(self):
        """ Test description """
        self.assertIsInstance(self.plc.description, str)

    def test_number_rooms(self):
        """ Test number of rooms """
        self.assertIsInstance(self.plc.number_rooms, int)

    def test_number_bathrooms(self):
        """ Test number of bathrooms """
        self.assertIsInstance(self.plc.number_bathrooms, int)

    def test_max_guest(self):
        """ Test max number of guest """
        self.assertIsInstance(self.plc.max_guest, int)

    def test_price_by_night(self):
        """ Test price by night """
        self.assertIsInstance(self.plc.price_by_night, int)

    def test_latitude(self):
        """ Test latitude """
        self.assertIsInstance(self.plc.latitude, float)

    def test_longitude(self):
        """ Test longitude """
        self.assertIsInstance(self.plc.longitude, float)

    def test_amenity_ids(self):
        """ Test amenity ids"""
        self.assertIsInstance(self.plc.amenity_ids, list)
