#!/usr/bin/python3
import unittest
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage


class TestInitFile(unittest.TestCase):

    # Test if FileStorage is imported correctly
    def test_import_file_storage(self):
        self.assertIsInstance(storage, FileStorage)

    # Test if storage is initialized as an instance of FileStorage
    def test_storage_instance(self):
        self.assertIsInstance(storage, FileStorage)

    # Test if reload() method is called on storage
    @patch.object(FileStorage, 'reload')
    def test_reload_called(self, mock_reload):
        storage.reload()
        self.assertTrue(mock_reload.called)


if __name__ == '__main__':
    unittest.main()
