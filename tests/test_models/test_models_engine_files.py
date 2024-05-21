import os
import unittest
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel
import models


class TestFileStorage(unittest.TestCase):

    # Test if models/engine directory exists
    def test_engine_directory_exists(self):
        self.assertTrue(
            os.path.exists("models/engine"),
            "models/engine directory does not exist")

    # Test if models/engine/file_storage.py file exists
    def test_file_storage_file_exists(self):
        self.assertTrue(
            os.path.exists("models/engine/file_storage.py"),
            "models/engine/file_storage.py file does not exist")

    # Test if models/engine/file_storage.py file is not empty
    def test_file_storage_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/engine/file_storage.py") > 0,
            "models/engine/file_storage.py file is empty")

    # Test if models/engine/__init__.py file exists
    def test_engine_init_file_exists(self):
        self.assertTrue(
            os.path.exists("models/engine/__init__.py"),
            "models/engine/__init__.py file does not exist")

    # Test if models/engine/__init__.py file is empty
    def test_engine_init_file_empty(self):
        self.assertTrue(
            os.path.getsize("models/engine/__init__.py") == 0,
            "models/engine/__init__.py file is not empty")

    # Test if models/__init__.py file exists
    def test_models_init_file_exists(self):
        self.assertTrue(
            os.path.exists("models/__init__.py"),
            "models/__init__.py file does not exist")

    # Test if models/__init__.py file is not empty
    def test_models_init_file_not_empty(self):
        self.assertTrue(
            os.path.getsize("models/__init__.py") > 0,
            "models/__init__.py file is empty")


if __name__ == '__main__':
    unittest.main()
