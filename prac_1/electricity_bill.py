TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator 2.0')
tariff = input('Which tariff? 11 or 31: ')
daily_use = float(input('Enter daily use in kWh: '))
days = int(input('Enter number of billing days: '))
if tariff == '11':
    bill = (TARIFF_11 * daily_use) * days
else:
    bill = (TARIFF_31 * daily_use) * days
print(f'Estimate bill: ${bill:.2f}')
