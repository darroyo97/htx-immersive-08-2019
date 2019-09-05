def view_contacts(contacts):
    number_of_contacts = len(contacts)
    if number_of_contacts:
        print(f"Contacts ({number_of_contacts}):")
        for index, contact in enumerate(contacts):
            print(
                f"{index}. {contact['first_name']} {contact['last_name']}: {contact['phone']}")
    else:
        print('Cannot be found.')