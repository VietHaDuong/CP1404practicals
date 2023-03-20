total_price = 0
DISCOUNT = .1
DISCOUNT_THRESHOLD = 100
items = int(input('Number of items: '))
while items < 0:
    print('Invalid number of items!')
    items = int(input('Number of items: '))
for item in range(items):
    price = float(input('Price of item: '))
    total_price += price
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price - (total_price * DISCOUNT)
print(f'Total price for {items} items is {total_price:.2f}')

