class Contact(object):
    def __init__(self):
        self.contact = {}

    def add_contact(self, name, number):
        self.contact[name] = number
        if len(number) != 10:
            return {"info": "Re-enter the contact, contact must be 10 digits"}
        return {"info": "Contact added"}

    def delete_contact(self, name, number):
        self.contact[name] = number
        return {"info": "Contact deleted"}

    def update_contact(self, name, number, number2):
        self.number = number2
        self.contact[name] = number2
        return "My new contact is {}".format(number2)

    def view_contacts(self, name, number):
        self.contact[name] = number
        return "Contact for {} is {}".format(name, number)
