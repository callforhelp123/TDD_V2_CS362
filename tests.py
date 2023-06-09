import unittest
from check_pwd import check_pwd


class TestCheckPWD(unittest.TestCase):
    def test_empty_string(self):
        """tests if function rejects empty strings"""
        self.assertFalse(check_pwd(""))

    def test_length_of_7(self):
        """tests if function rejects length of 7"""
        self.assertFalse(check_pwd("aaaaaaa"))

    def test_length_of_21(self):
        """tests if function rejects length of 21"""
        self.assertFalse(check_pwd("aaaaaaaaaaaaaaaaaaaaa"))

    def test_lowercase(self):
        """tests if function rejects a string with no lowercase letters"""
        self.assertFalse(check_pwd("AAAAAAAA"))

    def test_uppercase(self):
        """tests if function rejects a string with no uppercase letters"""
        self.assertFalse(check_pwd("aaaaaaaaaa"))

    def test_no_digits(self):
        """tests if function rejects a string with no uppercase letters"""
        self.assertFalse(check_pwd("aaAAaaaaa"))

    def test_no_required_symbols(self):
        """tests if function rejects a string with no special symbols"""
        self.assertFalse(check_pwd("aaAAa2aaa"))


if __name__ == '__main__':
    unittest.main()
