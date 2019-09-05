from lookup import lookup
import contacts
import menu
import view
from add import add
selection = menu.menu_selection()

while selection != 5:
    if selection == 1:
        results = lookup(input('What name do you want to look up?'))
        print('Found.')
        view.view_contacts(results)
    elif selection == 2:
        add()
    elif selection == 3:
        pass
    elif selection == 4:
        pass
    elif selection != 5:
        menu.main_menu()
    else:
        print('Whoops, please try again')
        selection = menu.menu_selection()
    selection = menu.menu_selection()

print('Goodbye, thanks for using the phone book')

