from prac_6.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        part = line.strip().split(',')
        guitar = Guitar(part[0], part[1], part[2])
        guitars.append(guitar)
    guitars.sort()
    print(guitars)

    for guitar in guitars:
        print(guitar)


main()
