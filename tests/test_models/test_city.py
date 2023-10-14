#!/usr/bin/python3
"""
    Test class City
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ Test class for class City """

    def setUp(self):
        """ Set up a new city instance """
        self.cty = City()

    def tearDown(self):
        """ Clean up """
        del self.cty

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.cty, City)

    def test_state_id(self):
        """ Test state id """
        self.assertIsInstance(self.cty.state_id, str)

    def test_name(self):
        """ Test city name """
        self.assertIsInstance(self.cty.name, str)
