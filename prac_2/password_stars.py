def main():
    password = get_password()
    while len(password) < 5:
        print('Minimum password length is 5')
        password = get_password()
    generate_asterisks(password)


def generate_asterisks(password):
    print(len(password) * '*')


def get_password():
    password = input('Enter password: ')
    return password


main()
