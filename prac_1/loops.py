for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Print n stars
stars = int(input('Number of stars: '))
print('*' * stars)
print()

# Print n lines of increasing stars
for star in range(stars + 1):
    print(star * '*')