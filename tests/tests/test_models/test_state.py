#!/usr/bin/python3
"""
    Test class State
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test class for class State """

    def setUp(self):
        """ Set up a new state instance """
        self.st = State()

    def tearDown(self):
        """ Clean up """
        del self.st

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.st, State)

    def test_name(self):
        """ Test state name """
        self.assertIsInstance(self.st.name, str)
