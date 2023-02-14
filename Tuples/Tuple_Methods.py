
t1 = (1, 2, 3, 4)
i = t1.index(2)
print(f'2 is at position: {i}')

x = 1
for x in t1:
    i = t1.index(x)
    print(f'x is at index: {i}')
else:
    print(f'{x} not in tuple')

n = t1.count(2)
print(n)

print(100 in t1)
print(3 in t1)

print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2 = sorted(t1, reverse=True)
print(t2)












