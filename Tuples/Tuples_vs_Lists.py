
# tuples are faster than lists
# tuples are safer than lists
# tuples can be used as keys in dictionaries
# storage efficiency

import sys
l1 = [1, 2, 3, 4, 5, 6]
t1 = (1, 2, 3, 4, 5, 6)

print(f'List memory size: {sys.getsizeof(l1)}')
print(f'Tuple memory size: {sys.getsizeof(t1)}')
