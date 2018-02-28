import unittest
from contact import Contact

class PhonebookTestCase(unittest.TestCase):
    def test_add_contact(self):
        contact = Contact()
        result = contact.add_contact("0712351423")
        self.assertEqual(result["info"], "Contact added")

