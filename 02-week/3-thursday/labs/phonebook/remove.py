import contacts
import view
from lookup import lookup

def remove():
    view.view_contacts(contacts.contacts)
    choice = int(input('Enter the nubmer of the person you want to delete'))
    contacts.contacts.pop(choice)
    print('Deletion successful')