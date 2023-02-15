
import time
import sys
l1 = list(range(1_000_000))
start = time.time()
# print(start)
bv = 456789 in l1
end = time.time()
print(f'List lookup time: {end - start:.10f}')
print(f'List memory usage: {sys.getsizeof(l1)}')
print('#' * 50)

s1 = set(range(1_000_000))
start = time.time()
bv = 456789 in s1
end = time.time()
print(f'Set lookup time: {end - start:.10f}')
print(f'Set memory usage: {sys.getsizeof(s1)}')
print('#' * 50)













