import email
import unittest

from webinar5.accounts import *

class TestCleanName(unittest.TestCase):

    def test_strip_space(self):
        self.assertEqual(clean_name(" sveta "),
                         "Sveta")

    def test_capitalize(self):
        self.assertEqual(clean_name("sveta"),
                         "Sveta")

    def test_username(self):
        self.assertEqual(make_username
                         ("Sveta", "Sveta"),
                         "sveta_sveta")


class TestValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email
                        ("sveta123@gmail.com"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email
                         ("scdfer.gmail.com"))

    def test_email_contains_at_sign(self):
        self.assertTrue("@" in "sveta@gmail.com")


class TestUserProfile(unittest.TestCase):
    def setUp(self):
        self.user = {
            "name": "Sveta",
            "email": "sveta@gmaim.com",
            "roles": ["reader"],
        }

    def test_profile_has_name(self):
        self.assertEqual(self.user["name"],
                         "Sveta")

    def test_email_is_valid(self):
        self.assertTrue(is_valid_email
                        (self.user["email"]))

    def test_add_role(self):
        self.user["roles"].append("admin")
        self.assertIn("admin",
                      self.user["roles"])
        self.assertEqual(len(self
                             .user["roles"]),2)

    def test_count_roles(self):
        self.assertEqual(len(self.user["roles"]),
                         1)
# banana
# sky
# BANana
class TestCountVowels(unittest.TestCase):
    def test_vowels(self):
        self.assertEqual(count_vowels("BAnana"), 3)
        self.assertEqual(count_vowels("banana"), 3)
        self.assertEqual(count_vowels("sky"), 0)