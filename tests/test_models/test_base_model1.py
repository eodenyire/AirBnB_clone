import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_save_updates_updated_at(self):
        # Create an instance of BaseModel
        my_model = BaseModel()

        # Get the initial updated_at value
        initial_updated_at = my_model.updated_at

        # Call the save method
        my_model.save()

        # Get the updated updated_at value
        updated_updated_at = my_model.updated_at

        # Assert that the updated_at value has changed
        self.assertNotEqual(initial_updated_at, updated_updated_at)

        # Assert that the updated_updated_at is a datetime object
        self.assertIsInstance(updated_updated_at, datetime)

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

    def test_init_method(self):
        # Test the __init__ method of BaseModel
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_to_dict_method(self):
        # Test the to_dict method of BaseModel
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        self.assertIn('id', my_model_dict)
        self.assertIn('created_at', my_model_dict)
        self.assertIn('updated_at', my_model_dict)
        self.assertEqual(my_model_dict['id'], my_model.id)
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_model_dict['created_at'], str)
        self.assertIsInstance(my_model_dict['updated_at'], str)

    def test_str_method(self):
        # Test the __str__ method of BaseModel
        my_model = BaseModel()
        my_model_str = str(my_model)
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model_str, expected_str)


if __name__ == '__main__':
    unittest.main()
