from lookup import lookup
import contacts
import menu
import view
from add import add
from remove import remove
selection = menu.menu_selection()

while selection != 5:
    if selection == 1:
        results = lookup(input('What name do you want to look up?'))
        print('Found.')
        view.view_contacts(results)
    elif selection == 2:
        add()
    elif selection == 3:
        remove()
    elif selection == 4:
        view.view_contacts(contacts.contacts)
    elif selection != 5:
        menu.main_menu()
    else:
        print('Whoops, please try again')
        selection = menu.menu_selection()
    selection = menu.menu_selection()

print('Goodbye, thanks for using the phone book')

