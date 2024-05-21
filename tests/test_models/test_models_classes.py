import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
import models


class TestFilePresence(unittest.TestCase):

    # Test if models/user.py file exists
    def test_user_file_exists(self):
        self.assertTrue(
            os.path.exists("models/user.py"),
            "models/user.py file does not exist")

    # Test if models/user.py file is not empty
    def test_user_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/user.py") > 0,
            "models/user.py file is empty")

    # Test if models/state.py file exists
    def test_state_file_exists(self):
        self.assertTrue(
            os.path.exists("models/state.py"),
            "models/state.py file does not exist")

    # Test if models/state.py file is not empty
    def test_state_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/state.py") > 0,
            "models/state.py file is empty")

    # Test if models/city.py file exists
    def test_city_file_exists(self):
        self.assertTrue(
            os.path.exists("models/city.py"),
            "models/city.py file does not exist")

    # Test if models/city.py file is not empty
    def test_city_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/city.py") > 0,
            "models/city.py file is empty")

    # Test if models/amenity.py file exists
    def test_amenity_file_exists(self):
        self.assertTrue(
            os.path.exists("models/amenity.py"),
            "models/amenity.py file does not exist")

    # Test if models/amenity.py file is not empty
    def test_amenity_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/amenity.py") > 0,
            "models/amenity.py file is empty")

    # Test if models/place.py file exists
    def test_place_file_exists(self):
        self.assertTrue(
            os.path.exists("models/place.py"),
            "models/place.py file does not exist")

    # Test if models/place.py file is not empty
    def test_place_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/place.py") > 0,
            "models/place.py file is empty")

    # Test if models/review.py file exists
    def test_review_file_exists(self):
        self.assertTrue(
            os.path.exists("models/review.py"),
            "models/review.py file does not exist")

    # Test if models/review.py file is not empty
    def test_review_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/review.py") > 0,
            "models/review.py file is empty")


if __name__ == '__main__':
    unittest.main()
