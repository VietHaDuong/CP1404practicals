import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45
number_of_pick = int(input('How many quick picks? '))
for pick in range(number_of_pick):
    numbers = []
    for count in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        numbers.append(number)
    numbers.sort()
    print(' '.join(f'{number:2}' for number in numbers))

