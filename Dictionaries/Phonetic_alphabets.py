
alphabet = dict()

my_str = 'abcdef'.upper()
print(my_str, end=' => ')

#for char in my_str:
 #   print(alphabet[char], end='    ')

countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}

# List of keys sorted in alphabetical order
keys = sorted(countries.keys())

# Iterate over the keys and print the corresponding value of the dictionary
for k in keys:
    print(countries[k])