import unittest
import os

class TestProjectFiles(unittest.TestCase):
	def test_readme_file_exists(self):
		self.assertTrue(os.path.exists("README.md"), "README.md file not found")

	def test_authors_file_exists(self):
		self.assertTrue(os.path.exists("AUTHORS"), "AUTHORS file not found")
	
	def test_test_directory_exists(self):
		self.assertTrue(os.path.exists("tests"), "tests directory not found")

if __name__ == '__main__':
	unittest.main()
