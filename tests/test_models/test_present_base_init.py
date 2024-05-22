#!/usr/bin/python3
import os
import unittest
from models.base_model import BaseModel
import models
from models.engine.file_storage import FileStorage


class TestModels(unittest.TestCase):

    # Test if models directory exists
    def test_models_directory_exists(self):
        self.assertTrue(
            os.path.exists("models"),
            "models directory does not exist")

    # Test if models/base_model.py file exists
    def test_base_model_file_exists(self):
        self.assertTrue(
            os.path.exists("models/base_model.py"),
            "models/base_model.py file does not exist")

    # Test if models/base_model.py file is not empty
    def test_base_model_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/base_model.py") > 0,
            "models/base_model.py file is empty")

    # Test if models/__init__.py file exists
    def test_init_file_exists(self):
        self.assertTrue(
            os.path.exists("models/__init__.py"),
            "models/__init__.py file does not exist")

    # Test if models/__init__.py file is not empty
    def test_init_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/__init__.py") > 0,
            "models/__init__.py file is empty")


if __name__ == '__main__':
    unittest.main()
