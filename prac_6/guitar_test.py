from prac_6.guitar import Guitar


def main():
    Gibson = Guitar('Gibson L-5 CES', 1922, 16035.40)
    Yamaha = Guitar('Yamaha Pacifica 611VFM', 1990, 988)

    print(Gibson)
    print(Gibson.get_age(), Gibson.is_vintage())

    print(Yamaha)
    print(Yamaha.get_age(), Yamaha.is_vintage())


main()
