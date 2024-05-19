#!/usr/bin/python3
"""
Contains the TestPlaceDocs and TestPlace classes
"""

from datetime import datetime
import inspect
from models import place
from models.base_model import BaseModel
import pycodestyle
import unittest
Place = place.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8s = pycodestyle.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

class TestPlace(unittest.TestCase):
    """Test the Place class"""
    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_name_attr(self):
        """Test that Place has attribute name, and it's as an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        pl = Place()
        new_d = pl.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in pl.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        pl = Place()
        new_d = pl.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], pl.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], pl.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))

