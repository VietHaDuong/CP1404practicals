MENU ="""(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    score = get_valid_score()
    choice = input('>>> ').lower()
    while choice != 'q':
        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            print(determine_grade(score))
        elif choice == 's':
            generating_stars(score)
        choice = input('>>> ').lower()
    print('Goodbye!')


def generating_stars(score):
    print(score * '*')


def get_valid_score():
    score = int(input('Enter score: '))
    while score < 0 or score > 100:
        print('Invalid score!')
        score = int(input('Enter score: '))
    return score


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()

