#!/usr/bin/python3
"""
    Test class Amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test class for class Amenity """

    def setUp(self):
        """ Set up a new amenity instance """
        self.amt = Amenity()

    def tearDown(self):
        """ Clean up """
        del self.amt

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.amt, Amenity)

    def test_name(self):
        """ Test amenity name """
        self.assertIsInstance(self.amt.name, str)
