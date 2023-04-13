FILENAME = 'wimbledon.csv'
INDEX_COUNTRY = 1
INDEX_WINNER = 2


def main():
    records = get_records()
    champions_and_wins, countries = process_records(records)
    display_result(champions_and_wins, countries)


def get_records():
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


def process_records(records):
    champion_and_wins = dict()
    countries = set()
    for record in records:
        countries.add(record[INDEX_COUNTRY])
        try:
            champion_and_wins[record[INDEX_WINNER]] += 1
        except KeyError:
            champion_and_wins[record[INDEX_WINNER]] = 1
    return champion_and_wins, countries


def display_result(winner, countries):
    print('Wimbledon Champions:')
    for name, count in winner.items():
        print(name, count)
    print(f'These {len(countries)} countries have won Wimbledon:')
    print(', '.join(country for country in countries))


main()
