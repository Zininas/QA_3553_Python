import unittest


def check_password_length(password):
    if len(password)<8:
        raise ValueError ("Password is too short")
    return True

class TestCheckPasswordLength(unittest.TestCase):
    #list = [1,2,3,4,5]

    def test_short_password_raises_error(self):
        with self.assertRaises(ValueError):
            check_password_length("123")

    def test_valid_password_returns_true(self):
        self.assertTrue(check_password_length("query123"))