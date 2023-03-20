import random


def main():
    score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(0, 100)
    print(f'Random score: {random_score}')
    print(determine_grade(random_score))


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

