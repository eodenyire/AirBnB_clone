import unittest
from datetime import datetime
from models.base_model import BaseModel
import models
from io import StringIO


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

    def test_str_base_model(self):
        # test the printing of string representation of class
        my_model = BaseModel()
        my_model.name = 'my first model'
        my_model.number = 98
        created_at = my_model.created_at.isoformat()
        updated_at = my_model.updated_at.isoformat()
        expected_output = f"
        [BaseModel]({my_model.id})
        {{'id': '{my_model.id}',
            'created_at':
            datetime.datetime({my_model.created_at.year},
                              {my_model.created_at.month},
                              {my_model.created_at.day},
                              {my_model.created_at.hour},
                              {my_model.created_at.minute},
                              {my_model.created_at.second},
                              {my_model.created_at.microsecond}),
            'updated_at':
            datetime.datetime({my_model.updated_at.year},
                              {my_model.updated_at.month},
                              {my_model.updated_at.day},
                              {my_model.update_at.hour},
                              {my_model.updated_at.minute},
                              {my_model.updated_at.second},
                              {my_model.updated_at.microsecond}),
            'name': 'my first model', 'number': '98'}}"
        with patch('sys.stdout', new=StringIO()) as f:
            print(my_model)
            output = f.getvalue()

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
