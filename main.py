from services.contacts_service import createNewContact, loadContacts, listAllContacts, saveContacts, contactFile
from services.cloud_service import uploadToS3

def menu():
    print("------ Main Menu ------")
    print(" 1. Create a new contact")
    print(" 2. Contacts list")
    print(" 3. Save Contacts")
    print(" 4. Upload contacts to the cloud")
    print(" *. Close the program")
    print("-----------------------")

def uploadContacts():
    uploadToS3(contactFile)

def goodbye():
    print("Goodbye!")

def runProgram():
    answer = None
    stopProgram = False

    while stopProgram is not True:
        menu()
        answer = input("Select an action by number : ")

        if answer == "1":
            createNewContact()
        elif answer == "2":
            listAllContacts()
        elif answer == "3":
            saveContacts()
        elif answer == "4":
            uploadContacts()
        elif answer == "*":
            goodbye()
            stopProgram = True
        else:
            print(f"{answer} is not a valid choice.")
            answer = input("Select an action by number : ")

loadContacts()
runProgram()