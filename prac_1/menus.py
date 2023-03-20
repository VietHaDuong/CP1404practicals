menus = """(H)ello
(G)oodbye
(Q)uit"""

name = input('Enter name: ')
print(menus)
choice = input(">>> ").lower()
while choice != 'q':
    if choice == 'h':
        print(f'Hello {name}')
    elif choice == 'g':
        print(f'Goodbye {name}')
    else:
        print('Invalid choice')
    print(menus)
    choice = input(">>> ").lower()
print('Finished.')

