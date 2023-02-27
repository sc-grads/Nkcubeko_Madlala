l1 = [1, 2, 3]
l2 = l1
l2[0] = 'XX'
l2.append(10)
print(f'l2: {l2}')
print(f'l1: {l1}')

print(id(l1), id(l2))
l1.remove(2)
print(f'l2: {l2}')

l3 = l1.copy()
l3.append('abc')
print(f'l1: {l1}')
print(f'l3: {l3}')
print(id(l1), id(l3))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2]

new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(new_list)

my_list = [n for n in nums if n >= 5]
print(my_list)

















