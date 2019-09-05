#this will hold my main menu
def prompt_user():
    return int(input('"What do you want to do (1-5)?"'))

def main_menu():
    print('Electronic PhoneBook')
    print('========================')
    print('1. Look up an entry')
    print('2. Set an entry') 
    print('3. Delete an entry') 
    print('4. List all entries') 
    print('5. Quit')
    print('========================')


def menu_selection():
    main_menu()
    return prompt_user()

