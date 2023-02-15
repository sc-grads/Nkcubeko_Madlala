
l1 = [1, 3, 5, 7]
print(l1, id(l1))

l1 = l1 + [9, 11, 13]
print(l1, id(l1))

l1 += [15, 17]
print(l1, id(l1))

l1.extend((19, 21))
print(l1, id(l1))

l1.append(('a', 'b'))
print(l1, id(l1))

l2 = list('abcde')
print(l2, id(l2))
l3 = l2 * 3
print(l3)

print('#' * 10 + 'LIST SLICING' + '#' * 10)

number = [1, 2, 3, 4, 5]
num = number[1:4]
print(f'number: {number}')
print(f'num: {num}')

print(number[:3])
print(number[2:])
print(number[::3])

number[0:2] = ['a', 'b']
print(number)
number[0:2] = ['x', 'y', 'z']
print(number)

ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']
for ip in ip_list:
    print(f'Connecting to {ip} ...')


print('10.0.0.1' in ip_list)
print('10.0.0.1' not in ip_list)
print('10' in ip_list)





