MENU ="""(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    print(MENU)
    choice = input('>>> ').lower()
    while choice != 'q':
        option(choice)
    print('Goodbye!')


def option(choice):
    if choice == 'g':
        score = get_score()
    elif choice == 'p':
        print(determine_grade(score))
    elif choice == 's':
        generating_stars()


def generating_stars():
    print(score * '*')


def get_score():
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

