#!/usr/bin/python3
import models
from time import sleep
import unittest
from datetime import datetime
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
from models import storage

class TestBaseModel(unittest.TestCase):
    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_save_method(self):
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_two_saves(self):
        bm = BaseModel()
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)

    def test_save_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)

    def test_save_updates_file(self):
        bm = BaseModel()
        bm.save()
        bmid = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bmid, f.read())

    def test_to_dict_method(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 89
        d = bm.to_dict()
        self.assertEqual(d["id"], bm.id)
        self.assertEqual(d["__class__"], type(bm).__name__)
        self.assertEqual(d["created_at"], bm.created_at.isoformat())
        self.assertEqual(d["updated_at"], bm.updated_at.isoformat())
        self.assertEqual(d["name"], bm.name)
        self.assertEqual(d["my_number"], bm.my_number)

    def test_to_dict_with_arg(self):
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.to_dict(None)

    def test_contrast_to_dict_dunder_dict(self):
        bm = BaseModel()
        self.assertNotEqual(bm.to_dict(), bm.__dict__)

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr= bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

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

        expected_output = (
            f"[BaseModel] ({my_model.id}) {{'id': '{my_model.id}', 'created_at': datetime.datetime("
            f"{my_model.created_at.year}, {my_model.created_at.month}, {my_model.created_at.day}, "
            f"{my_model.created_at.hour}, {my_model.created_at.minute}, {my_model.created_at.second}, "
            f"{my_model.created_at.microsecond}), 'updated_at': datetime.datetime("
            f"{my_model.updated_at.year}, {my_model.updated_at.month}, {my_model.updated_at.day}, "
            f"{my_model.updated_at.hour}, {my_model.updated_at.minute}, {my_model.updated_at.second}, "
            f"{my_model.updated_at.microsecond}), 'name': 'my first model', 'number': 98}}"
        )

        with patch('sys.stdout', new=StringIO()) as f:
            print(my_model)
            output = f.getvalue().strip()

        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
