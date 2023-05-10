import unittest
from check_pwd import check_pwd


class TestCheckPWD(unittest.TestCase):
    def test_empty_string(self):
        """tests if function rejects empty strings"""
        self.assertFalse(check_pwd(""))

    def test_length_of_7(self):
        """tests if function rejects length of 7"""
        self.assertFalse(check_pwd("aaaaaaa"))


if __name__ == '__main__':
    unittest.main()
