# l1 = list()
# print(dir(l1))
# help(l1.append())

l1 = [1, 2.2, 'abc', 24]
l1.append(5)
print(l1)
l1.append([6,7])
print(l1)
l1.insert(1, 33)
print(l1)

years = [2020, 2022, 2023]
years.insert(1, 2022)
years.insert(len(years), 2024)
print(years)

years.clear()
print(years)

l2 = [10, 11, 13, 14]
x = l2.pop()
print(x)
print(l2)
y = l2.pop(1)
print(y, l2)

l3 = [1, 2, 1, 6, 2, 3, 1]
l3.remove(1)
print(l3)

while 1 in l3:
    l3.remove(1)
print(l3)

print('*' * 20 + ' SLICING METHODS - PART 2 ' + '*' * 20)

names = ['John', 'Dan', 'Tom', 'John', 'Bill']
i = names.index('Tom')
print(f'Tom is at index {i}')

letters = list('adadjkhaajajjngnivcbx')
n = letters.count('j')
print(n)
print('z' in letters)


lst = [1, 3, 'abc', 10, 'x']
lst.reverse()
print(f'lst: {lst}')

ages = [12, 4, 17,23, 20, 9,]
la = sorted(ages)
print(ages)
print(la)

nl = ages.sort()
print(nl)
print(ages)
ages.sort(reverse=True)
print(ages)

lb = [-3, 2, 120, 10, 5, 14]
print(f'max: {max(lb)}')
print(f'min: {min(lb)}')
print(f'sum: {sum(lb)}')

















