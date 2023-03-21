MINIMUM_LENGTH = 5


def main():
    password = get_password(MINIMUM_LENGTH)
    generate_asterisks(password)


def get_password(length):
    password = input('Enter password: ')
    while len(password) < length:
        print(f'Minimum password length is {length}')
        password = input('Enter password: ')
    return password


def generate_asterisks(password):
    print(len(password) * '*')


main()
