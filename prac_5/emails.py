names_emails = dict()
email = input('Email: ')
while email != '':
    name = ' '.join(email.split('@')[0].split('.')).title()
    confirmation = input(f'Is your name {name}? (Y/n) ').lower()
    if confirmation != 'y' and confirmation != '':
        name = input('Name: ')
    names_emails[email] = name
    email = input('Email: ')

print()
for email, name in names_emails.items():
    print(f'{name} ({email})')
