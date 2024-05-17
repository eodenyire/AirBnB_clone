import unittest
import os

class TestProjectFiles(unittest.TestCase):
    def test_readme_exists(self):
        self.assertTrue(os.path.exists("README.md"), "README.md file not found")

    def test_authors_exists(self):
        self.assertTrue(os.path.exists("AUTHORS"), "AUTHORS file not found")

    def test_test_directory_exists(self):
        self.assertTrue(os.path.exists("tests"), "tests directory not found")

    def test_base_model_files_exist(self):
        self.assertTrue(os.path.exists("models/base_model.py"), "models/base_model.py file not found")
        self.assertTrue(os.path.exists("models/_init.py"), "models/init_.py file not found")
        self.assertTrue(os.path.exists("tests/test_base_model.py"), "tests/test_base_model.py file not found")

    def test_file_storage_files_exist(self):
        self.assertTrue(os.path.exists("models/engine/file_storage.py"), "models/engine/file_storage.py file not found")
        self.assertTrue(os.path.exists("models/engine/_init.py"), "models/engine/init_.py file not found")
        self.assertTrue(os.path.exists("tests/test_file_storage.py"), "tests/test_file_storage.py file not found")

    def test_console_file_exists(self):
        self.assertTrue(os.path.exists("console.py"), "console.py file not found")

    def test_user_files_exist(self):
        self.assertTrue(os.path.exists("models/user.py"), "models/user.py file not found")
        self.assertTrue(os.path.exists("tests/test_user.py"), "tests/test_user.py file not found")

    def test_other_model_files_exist(self):
        # Assuming each model has its own test file
        model_files = ["state.py", "city.py", "amenity.py", "place.py", "review.py"]
        for model_file in model_files:
            self.assertTrue(os.path.exists(f"models/{model_file}"), f"models/{model_file} file not found")
            self.assertTrue(os.path.exists(f"tests/test_{model_file}"), f"tests/test_{model_file} file not found")

    def test_console_and_file_storage_integration(self):
        # Integration test to ensure console.py and file_storage.py are properly integrated
        console_file = "console.py"
        file_storage_file = "models/engine/file_storage.py"
        self.assertTrue(os.path.exists(console_file), f"{console_file} file not found")
        self.assertTrue(os.path.exists(file_storage_file), f"{file_storage_file} file not found")
        # Perform integration tests here as needed

if _name_ == '_main_':
    unittest.main()
