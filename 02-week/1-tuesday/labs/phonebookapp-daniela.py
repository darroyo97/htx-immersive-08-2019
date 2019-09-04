def print_menu():
    print('========================')
    print('1. Look up an entry')
    print('2. Set an entry') 
    print('3. Delete an entry') 
    print('4. List all entries') 
    print('5. Quit') 
    
phonebook = {
    'Jon': '123-123-1234',
    'Sansa': '321-321-4321',
    'Ayra': '456-456-4567',
}
menu_choice = 0
print_menu()

while menu_choice != 5:
    menu_choice = int(input("What do you want to do (1-5)?"))
    if menu_choice == 1:
        print("Look up an entry")
        search_user = input("Name:")
        if search_user in phonebook:
            print(phonebook[search_user])
    elif menu_choice == 2:
        print("Add Name and Number")
        new_user = input("Name: ")
        new_user_number = input("Number: ")
        phonebook[new_user] = new_user_number
    elif menu_choice == 3:
        print("Delete an entry")
        delete_user = input("Name: ")
        if delete_user in phonebook:
            phonebook.pop(delete_user)
    elif menu_choice == 4:
        print("List all entries")
        for x in phonebook.keys():
            print("Name: ", x, "Number", phonebook[x])
        print()
    elif menu_choice != 5:
        print_menu    

         