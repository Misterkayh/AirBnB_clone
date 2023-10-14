#!/usr/bin/python3
"""
    Test class Review
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test class for class Review """

    def setUp(self):
        """ Set up a new review instance """
        self.rvy = Review()

    def tearDown(self):
        """ Clean up """
        del self.rvy

    def test_instance(self):
        """ Test instance """
        self.assertIsInstance(self.rvy, Review)

    def test_place_id(self):
        """ Test place id """
        self.assertIsInstance(self.rvy.place_id, str)

    def test_user_id(self):
        """ Test user id """
        self.assertIsInstance(self.rvy.user_id, str)

    def test_text(self):
        """ Test text """
        self.assertIsInstance(self.rvy.text, str)
