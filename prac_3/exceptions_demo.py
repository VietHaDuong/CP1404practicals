"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print('Try again!')
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"""
1.When will a ValueError occur?
ValueError occurs when a function is called but with an incorrect value

2.When will a ZeroDivisionError occur?
ZeroDivisionError occur when a number is attempted to be divided by 0

3.Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, by implementing a while loop
"""