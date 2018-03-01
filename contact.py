class Contact(object):
    def __init__(self):
        self.contact = {}

    def add_contact(self, name, number):
        self.contact[name] = number
        return {"info": "Contact added"}

    def delete_contact(self, name, number):
        self.contact[name] = number
        return {"info": "Contact deleted"}
