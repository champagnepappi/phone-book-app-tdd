class Contact:
    def __init__(self):
        self.contact = {}

    def add_contact(self, number):
        self.contact[number] = number
        return {"info": "Contact added"}
