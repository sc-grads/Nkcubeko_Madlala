
s1 = {1, 3, 5}
s2 = {5, 7, 9}
s3 = s1.intersection(s2)
print(f's3: {s3}')
s3 = s1 & s2
print(f's3: {s3}')

s4 = s1.difference(s2)
print(f's4: {s4}')
s4 = s1 - s2
print(f's4: {s4}')

s5 = s1.symmetric_difference(s2)
print(f's5: {s5}')
s5 = s1 ^ s2
print(f's5: {s5}')

s6 = s1.union(s2)
print(f's6: {s6}')
s6 = s1 | s2
print(f's6: {s6}')

st1 = {1, 3, 5}
st2 = {5, 7, 9}
print(st1.isdisjoint(st2))
st3 = {8, 9}
print(st1.isdisjoint(st3))

print({1, 3} < {1, 2, 3, 4})




























