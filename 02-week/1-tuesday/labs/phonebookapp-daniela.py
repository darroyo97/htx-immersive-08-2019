phonebook = {
    'Jon': '123-123-1234',
    'Sansa': '321-321-4321',
    'Ayra': '456-456-4567',
}
# This searches for a user
search_user = input("Enter name here:")
print(phonebook[search_user])

#This adds new user with number

new_user_name = input("New concact name")
new_user_number = input("New number for user")
phonebook[new_user_name] = new_user_number
print(phonebook)

#This deletes a user
delete_user = input("Name of user you want to delete")
phonebook.pop(delete_user)
print(phonebook)

#To print all enteries 

print_all = ("Do you wish to print all contacts? Yes/No")

if print_all == 'Yes':
    print(phonebook)
else:
    print("OK")






