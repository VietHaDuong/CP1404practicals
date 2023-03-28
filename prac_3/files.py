# Code ask for user's name
name = input('Enter name: ')
out_file = open('name.txt', 'w')
out_file.write(name)
out_file.close()

# Code that open file and read name
in_file = open('name.txt', 'r')
print(f'Your name is {in_file.read().strip()}')

# Code that open file and read the first 2 numbers then print the sum of that 2 numbers
read_file = open('numbers.txt', 'r')
first_number = int(read_file.readline())
second_number = int(read_file.readline())
read_file.close()
print(first_number + second_number)

# Print total sum of all numbers
in_file = open('numbers.txt', 'r')
total = 0
for line in in_file:
    total += int(line)
in_file.close()
print(total)
