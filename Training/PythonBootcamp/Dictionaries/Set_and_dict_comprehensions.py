
names = {'Tom', 'ANNE', 'johN', 'dAn'}
names = {n.capitalize() for n in names}
print(names)

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {k*2: v*2 for k,v in d1.items()}
print(d2)

d3 = {k.upper(): v*2 for k,v in d1.items()}
print(d3)
d4 = {k.upper(): v*2 for k,v in d1.items() if v % 3 == 0}
print(d4)

years = {2017, 2018, 2019}
revenues = {3000, 4000, 5000}
z = zip(years, revenues)
sales = list(z)
print(sales)

my_sales = dict(zip(years, revenues))
print(my_sales)

profit = {k: v*0.15 for k,v in my_sales.items()}
print(profit)

salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}

taxes = {k: v * 0.1 for k, v in salaries.items()}
print(taxes)  # => {'John': 5000.0, 'Anne': 6600.0, 'Antonio': 4800.0}












