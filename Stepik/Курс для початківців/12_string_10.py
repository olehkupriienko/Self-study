s = 'In {0}, someone paid {1} {2} for two pizzas.'
year, amount, currency = '2010', '10k', 'Bitcoin'
print(s.format(year, amount, currency))

year = 2010
amount = '10K'
currency = 'Bitcoin'

print(f'In {year}, someone paid {amount} {currency} for two pizzas.')