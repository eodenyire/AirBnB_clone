import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_create_base_model_from_dict(self):
        # Create a dictionary representation of a BaseModel instance
        my_model_json = {
            'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            'created_at': '2017-09-28T21:03:54.052298',
            'my_number': 89,
            'updated_at': '2017-09-28T21:03:54.052302',
            'name': 'My_First_Model'
        }

        # Create a new BaseModel instance from the dictionary
        my_new_model = BaseModel(**my_model_json)

        # Check if the id attribute matches
        self.assertEqual(my_model_json['id'], my_new_model.id)

        # Check if the created_at attribute is a datetime object
        self.assertIsInstance(my_new_model.created_at, datetime)

        # Check if the name attribute matches
        self.assertEqual(my_model_json['name'], my_new_model.name)

        # Check if the my_number attribute matches
        self.assertEqual(my_model_json['my_number'], my_new_model.my_number)

        # Check if the updated_at attribute is a datetime object
        self.assertIsInstance(my_new_model.updated_at, datetime)

    def test_link_to_file_storage(self):
        # Create an instance of BaseModel
        my_model = BaseModel()

        # Ensure that the storage variable is properly linked
        self.assertEqual(storage.all()["BaseModel." + my_model.id], my_model)

        # Call the save method
        my_model.save()

        # Ensure that the save method of storage is called
        self.assertTrue(storage.all())

        # Create a new BaseModel instance
        my_new_model = BaseModel()

        # Ensure that new() method of storage is called for a new instance
        self.assertIn("BaseModel." + my_new_model.id, storage.all())


if __name__ == '__main__':
    unittest.main()
