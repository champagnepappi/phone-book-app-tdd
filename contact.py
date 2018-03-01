class Contact(object):
    def __init__(self):
        self.contact = {}

    def add_contact(self, number):
        self.contact[number] = number
        return {"info": "Contact added"}

    def delete_contact(self, number):
        self.contact[number] = number
        return {"info": "Contact deleted"}
