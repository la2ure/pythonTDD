import unittest
import string


# Create a function to encrypt a string
def encrypt(message, key):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    key = key * (len(message) // len(key)) + key[: len(message) % len(key)]
    encrypted_message = "".join(
        [
            abc[(abc.find(char) + abc.find(key[idx])) % len(abc)]
            # Enumerate iterates on every character to stock both character and its index
            for idx, char in enumerate(message)
        ]
    )

    print(encrypted_message)
    return encrypted_message


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.my_message = "shake"

    def test_inputExist(self):
        self.assertIsNotNone(self.my_message)

    def test_inputType(self):
        self.assertIsInstance(self.my_message, str)

    def test_functionReturnSomething(self):
        self.assertIsNotNone(encrypt(self.my_message, "milk"))

    def test_lenIO(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message, "milk")))

    def test_differentIO(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message, "milk"))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.my_message, "milk"), str)

    def test_shiftedCipher(self):
        encrypted_message = encrypt(self.my_message, "milk")
        self.assertNotEqual(self.my_message, encrypted_message)


if __name__ == "__main__":
    unittest.main()
