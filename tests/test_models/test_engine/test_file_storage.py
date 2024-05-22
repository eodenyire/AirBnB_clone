#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all_method_returns_correct_objects(self):
        """Test if all() returns all objects stored in __objects."""
        # Create some objects and add them to __objects
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)

        # Check if all() returns the correct objects
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + model1.id, all_objs)
        self.assertIn("BaseModel." + model2.id, all_objs)

    def test_new_method_sets_object_with_correct_key(self):
        """Test if new() properly sets
        an object in __objects with the correct key."""
        # Create an object and add it using new()
        model = BaseModel()
        self.storage.new(model)

        # Check if the object exists in __objects with the correct key
        self.assertIn("BaseModel." + model.id, self.storage.all())

    def test_save_method_serializes_objects_to_json_file(self):
        """Test if save() properly serializes __objects to a JSON file."""
        # Create some objects and add them to __objects
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)

        # Call save() and check if the JSON file contains the correct data
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn("BaseModel." + model1.id, data)
            self.assertIn("BaseModel." + model2.id, data)

    def test_reload_method_deserializes_json_file_to_objects(self):
        """Test if reload() properly deserializes
        the JSON file to __objects."""
        # Create some objects and add them to __objects
        model1 = BaseModel()
        model2 = BaseModel()
        self.storage.new(model1)
        self.storage.new(model2)

        # Call save() to save them to the JSON file
        self.storage.save()

        # Clear __objects and call reload()
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Check if __objects contains the correct objects after reloading
        all_objs = self.storage.all()
        self.assertIn("BaseModel." + model1.id, all_objs)
        self.assertIn("BaseModel." + model2.id, all_objs)

    def test_get_classes_method_returns_expected_class_name(self):
        """Test get_attr_name_from_classes method."""
        value_check = 'User'
        value = self.storage.get_attr_name_from_classes(value_check)
        self.assertEqual(value.__name__, value_check)


if __name__ == '__main__':
    unittest.main()
