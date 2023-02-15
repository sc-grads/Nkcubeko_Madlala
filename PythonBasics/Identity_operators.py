numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(20)
print(numbers)

nums = numbers.copy()
print(nums == numbers)
print(nums is numbers)
