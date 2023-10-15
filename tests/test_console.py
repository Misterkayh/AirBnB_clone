#!/usr/bin/python3
"""
    Test for Console
"""
import unittest
import pycodestyle


class TestHBNBCommand(unittest.TestCase):
    """ Class for testing HBNBCommand """

    def test_pep_conformance(self):
        """ Test pep conformance """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        check_pystyle = pystyle.check_files(["console.py",
                                            "tests/test_console.py"])
        self.assertEqual(check_pystyle.total_errors, 0)

    def test_module_doc(self):
        """ Test module documentation """
        mod_doc = __import__('console').__doc__
        self.assertGreater(len(mod_doc), 1)

    def test_class_doc(self):
        """ Test class documentation """
        class_doc = __import__('console').HBNBCommand.__doc__
        self.assertGreater(len(class_doc), 1)
