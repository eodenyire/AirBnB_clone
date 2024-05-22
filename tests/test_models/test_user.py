#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_attributes_exist(self):
        """Test that the User class has the expected attributes"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_default_values(self):
        """Test that the default values of attributes are empty strings"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_setting_attributes(self):
        """Test that attributes can be set correctly"""
        user = User()
        user.email = "test@example.com"
        user.password = "securepassword"
        user.first_name = "John"
        user.last_name = "Doe"
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "securepassword")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_init_with_kwargs(self):
        """Test that User can be initialized with keyword arguments"""
        kwargs = {
            "email": "test@example.com",
            "password": "securepassword",
            "first_name": "John",
            "last_name": "Doe"
        }
        user = User(**kwargs)
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "securepassword")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

if __name__ == '__main__':
    unittest.main()
