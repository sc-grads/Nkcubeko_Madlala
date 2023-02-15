
s1 = {1, 2, 3, 'a', 'b', 4, 1, 2, 'a', 3, 10}
print(s1)

s1.add((10, 20))
print(s1)

s1.remove('a')
print(s1)

# l1 = [1, 2]
s2 = set()
s3 = {}
print(type(s1), type(s2), type(s3))

s4 = set('hellooooo!')
print(s4)
s5 = set((1, 2, 3, 4, 4, 'abc'))
print(s5)

l2 = [10, 20, 30, 40]
s6 = set(l2)
print(s6)

macs = ['E4-A4-71-01-1B-15', 'E4-A4-71-01-1B-15', 'E4-A4-71-01-1B-15', 'E4-A4-71-01-1B-15',
        'E4-A4-71-01-1B-15', 'E4-A4-71-01-1B-20']
mac_addresses = set(macs)
print(mac_addresses)

for item in s4:
        print(item)
print('x' in s4)







