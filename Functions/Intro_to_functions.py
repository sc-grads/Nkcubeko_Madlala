
def my_fuction():
    print('Hello Python World')
    x = 3
    print(x**x)

my_fuction()


def vowel_count(my_str):
    """
    This function counts the number of vowels in a string
    """
    vowels = 'aeiou'
    my_str = my_str.lower()  # ignoring the case (we consider only lower-case letters)

    # Dictionary that stores the result.
    result = dict()

    for char in my_str:
        if char in vowels:
            if char in result.keys():
                result[char] += 1
            else:
                result[char] = 1

    return result


r = vowel_count('Awesome')
print(r)  # => {'a': 1, 'e': 2, 'o': 1}


def counter(my_str):
    vowels = 'aeiou'
    no_of_vowels = 0

    # letter case doesn't matter
    my_str = my_str.lower()  # make a lowercase copy of my_str

    for char in vowels:
        no_of_vowels += my_str.count(char)

    no_of_consonants = len(my_str) - no_of_vowels

    return (no_of_vowels, no_of_consonants)


print(counter('Python'))  # => (1, 5)
print(counter('BeautifUl'))  # => (5, 4)

r = vowel_count('Wow! Python is great!')
print(r)  # => {'o': 2, 'i': 1, 'e': 1, 'a': 1}

















