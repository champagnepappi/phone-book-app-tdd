import unittest
from contact import Contact

class PhonebookTestCase(unittest.TestCase):
    def test_add_contact(self):
        contact = Contact()
        result = contact.add_contact("pete", "0712351423")
        self.assertEqual(result["info"], "Contact added")

    def test_delete_contact(self):
        contact = Contact()
        result = contact.delete_contact("jane", "1873137103")
        self.assertEqual(result["info"], "Contact deleted")

