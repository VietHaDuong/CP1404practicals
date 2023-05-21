from prac_9.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 7)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
