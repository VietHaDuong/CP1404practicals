from prac_6.guitar import Guitar


def main():
    guitars = []
    print('My guitar!')
    name = input('Name: ')
    while name != '':
        year = int(input('Year: '))
        cost = float(input('Cost: '))
        adding_guitar = Guitar(name, year, cost)
        guitars.append(adding_guitar)
        print(adding_guitar, 'added.')
        name = input('Name: ')

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print('These are my guitars:')
    for count, guitar in enumerate(guitars, 1):
        vintage_tag = ''
        if guitar.is_vintage():
            vintage_tag = '(vintage)'
        print(f"Guitar {count}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_tag}")


main()
