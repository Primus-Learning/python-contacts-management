import json
from models.contact import Contact
from services.cloud_service import downloadContacts

contactFile = "data/contacts.json"
contacts = []

def loadContacts():
    try:
        f = open(contactFile, "r")
        content = f.read()
        f.close()

        if content != "":
            jsonContent = json.loads(content)
            for item in jsonContent:
                contacts.append(Contact(item["name"], item["phoneNumber"], item["email"]))

    except FileNotFoundError:
        downloadContacts("data/contacts.json")
        f = open(contactFile, "r")
        content = f.read()
        f.close()

        if content != "":
            jsonContent = json.loads(content)
            for item in jsonContent:
                contacts.append(Contact(item["name"], item["phoneNumber"], item["email"]))
    
def saveContacts():
    f = open(contactFile, "w")
    mapped = list(map(lambda x: x.toDict(), contacts))
    f.write(json.dumps(mapped))
    f.close()
    
    print("------")
    print(" The contacts file has been updated!")
    print("------")

def createNewContact():
    name = input("Enter contact's name : ")
    phoneNumber = input("Enter contact's phone number : ")
    email = input("Enter contact's email : ")

    contacts.append(Contact(name, phoneNumber, email))

def moreDetails(contactIndex: int):
    contact = contacts[contactIndex]
    print("------")
    print(f"  Contact Name         : {contact.name}")
    print(f"  Contact Phone Number : {contact.phoneNumber}")
    print(f"  Contact Email        : {contact.email}")
    print("------")


def listAllContacts():
    if len(contacts) == 0:
        print("------")
        print(" Contacts list is empty.")
        print("------")
        return
    
    for i in range(0, len(contacts)):
        contact = contacts[i]
        print(f" {i + 1}. {contact.name}")

    selectedContact = int(input("Enter a contact number to see more details or enter 0 to open the main menu : "))

    if selectedContact > 0:
        moreDetails(selectedContact - 1)