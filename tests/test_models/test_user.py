#!/usr/bin/python3
"""
    Test class User
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Test class for class User """

    def setUp(self):
        """ Set up a new user instance """
        self.usr = User()

    def tearDown(self):
        """ Clean up """
        del self.usr

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.usr, User)

    def test_email(self):
        """ Test email """
        self.assertIsInstance(self.usr.email, str)

    def test_password(self):
        """ Test password """
        self.assertIsInstance(self.usr.password, str)

    def test_first_name(self):
        """ Test first_name """
        self.assertIsInstance(self.usr.first_name, str)

    def test_last_name(self):
        """ Test last_name """
        self.assertIsInstance(self.usr.last_name, str)
