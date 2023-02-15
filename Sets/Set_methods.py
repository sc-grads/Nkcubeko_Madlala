
s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)
s1.remove(3)
print(s1)
s1.discard(1)
print(s1)
s1.discard(4)

x = s1.pop()
print(x, s1)

s2 = set('abc')
s3 = s2
s3.add('x')
print(s2)

s3.clear()
print(f's2: {s2}, s3: {s3}')

s4 = s1.copy()
s4.add('z')
print(f's4: {s4}, s1: {s1}')










