class Contact(object):
    def __init__(self):
        self.contact = {}

    def add_contact(self, name, number):
        self.contact[name] = number
        if len(number) != 10:
            return {"info": "Re-enter the contact"}
        return {"info": "Contact added"}

    def delete_contact(self, name, number):
        self.contact[name] = number
        return {"info": "Contact deleted"}
