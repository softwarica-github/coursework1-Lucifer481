import unittest
import os
from main import EncryptionTool  

class TestEncryptionTool(unittest.TestCase):
    def setUp(self):
        # Setup a temporary file for testing
        self.test_file = "test_file.txt"
        self.original_content = b"Hello, this is a testing."
        with open(self.test_file, 'wb') as f:
            f.write(self.original_content)

        # Initialize the EncryptionTool
        self.tool = EncryptionTool(self.test_file, 'dummy_key', 'dummy_salt')  
    def test_encryption(self):
        # Perform encryption
        self.tool.encrypt()

        # Assuming the encrypted file has a different name or path
        encrypted_file = "encrypted_" + self.test_file
        self.assertTrue(os.path.exists(encrypted_file))

        # Perform decryption
        self.tool.decrypt()

        # Verify if decrypted content matches the original content
        with open(self.test_file, 'rb') as f:
            decrypted_content = f.read()
        self.assertEqual(decrypted_content, self.original_content)

    def tearDown(self):
        # Clean up: remove any files created during the test
        os.remove(self.test_file)
        encrypted_file = "encrypted_" + self.test_file
        if os.path.exists(encrypted_file):
            os.remove(encrypted_file)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

