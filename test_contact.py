import unittest
from contact import Contact

class PhonebookTestCase(unittest.TestCase):
    def test_add_contact(self):
        contact = Contact()
        result = contact.add_contact("pete", "0712351423")
        self.assertEqual(result["info"], "Contact added")

    def test_add_contact_with_contact_greater_than_10_digits(self):
        contact = Contact()
        result = contact.add_contact("anne", "3414444444444414")
        self.assertNotEqual(result["info"], "Contact added")
        self.assertEqual(result["info"], "Re-enter the contact, contact must be 10 digits")

    def test_delete_contact(self):
        contact = Contact()
        result = contact.delete_contact("jane", "1873137103")
        self.assertEqual(result["info"], "Contact deleted")

    def test_update_contact(self):
        contact = Contact()
        contact.update_contact("jane", "34251617181", "5463727828")
        self.assertEqual(contact["jane"], "5463727828")



