class Contact:
    name: str
    phoneNumber: str
    email: str

    def __init__(self, name, phoneNumber, email) -> None:
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email
    
    def toDict(self):
        return {
            "name": self.name,
            "phoneNumber": self.phoneNumber,
            "email": self.email
        }
    