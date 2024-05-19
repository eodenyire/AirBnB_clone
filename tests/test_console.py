import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up storage after each test"""
        storage._FileStorage__objects.clear()

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual(f.getvalue(), '\n')

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual(f.getvalue(), '')

    def test_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            output = f.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertTrue(f"User.{output}" in storage.all().keys())

    def test_show_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn(f"[User] ({user_id})", output)

    def test_destroy_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"destroy User {user_id}")
            self.assertNotIn(f"User.{user_id}", storage.all())

    def test_all_no_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
            self.assertIn("[]", f.getvalue().strip())

    def test_all_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("all User")
            output = f.getvalue().strip()
            self.assertIn("[User]", output)

    def test_update_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attr_name(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            f.truncate(0)
            f.seek(0)
            self.console.onecmd(f"update User {user_id}")
            self.assertEqual(f.getvalue().strip(),
                "** attribute name missing **")

    def test_update_missing_attr_value(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            f.truncate(0)
            f.seek(0)
            self.console.onecmd(f"update User {user_id} first_name")
            output = f.getvalue().strip()
            self.assertEqual(output, "** value missing **")

    def test_update_valid(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(f"update User {user_id} first_name John")
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("first_name': 'John'", output)

    def test_update_dict(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd(
                f"update User {user_id} {{'first_name': 'John', 'age': 30}}")
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
            self.assertIn("first_name': 'John'", output)
            self.assertIn("age': 30", output)

    def test_count_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("MyModel.count()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_count_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            f.truncate(0)
            f.seek(0)
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "1")

if __name__ == '__main__':
    unittest.main()
