#this will hold my add functions
import contacts
import view
from lookup import lookup

def add():
    last_name = input('Last Name:')
    first_name = input('First Name:')
    phone_number = input('Phone Number:')
    contacts.contacts.append({
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone_number
    })
    print("New contact successfully added.")

    