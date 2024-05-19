import os
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    # Test if console.py file exists
    def test_console_file_exists(self):
        self.assertTrue(os.path.exists("console.py"), "console absent")

    # Test if console.py file is not empty
    def test_console_file_not_empty(self):
        self.assertTrue(os.path.getsize("console.py") > 0, "console empty")

    # Test quit command
    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(fake_out.getvalue().strip(), "", "Error in quit")

    # Test show command
    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("show BaseModel")
            self.assertEqual(
                fake_out.getvalue().strip(),
                "** instance id missing **",
                "Error in show")

    # Test destroy command
    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual(
                fake_out.getvalue().strip(),
                "** instance id missing **",
                "Error in destroy")

    # Test all command
    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all")
            self.assertTrue(
                fake_out.getvalue().strip().startswith("["),
                "Error in all command")

    # Test update command
    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("update BaseModel")
            self.assertEqual(
                fake_out.getvalue().strip(),
                "** instance id missing **",
                "Error in update")


if __name__ == '__main__':
    unittest.main()
