# Frozen Sets
fs1 = frozenset({1, 2, 3, 'a'})
print(fs1, type(fs1))

s1 = 'Python is cool!!'
fs2 = frozenset(s1)
print(fs2)
fs3 = frozenset() # empty frozenset

fst1 = frozenset([1, 2, 3, 4])
fst2 = frozenset([3, 4, 5, 6])
fst3 = fst1.intersection(fst2)
print(fst3)

ss1 = {4, 10, 20}
result1 = ss1.intersection(fst1)
result2 = fst1 - ss1

print(f'Result1 type: {type(result1)}')
print(f'Result2 type: {type(result2)}')










