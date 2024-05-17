# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel
import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime.datetime)
        self.assertIsInstance(model.updated_at, datetime.datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
    
    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn('id', model_str)
        self.assertIn('created_at', model_str)
        self.assertIn('updated_at', model_str)
    
    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

if __name__ == '__main__':
    unittest.main()
