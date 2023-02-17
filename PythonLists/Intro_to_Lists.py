
l1 = [1, 2.5, 'python', True, ['abc', 'xyz'], (4, 8, 12)]
print(len(l1))
l2 = [] #empty list
l3 = list() #empty list

print(l1[0])
x = l1[-1]
print(x)

my_str = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

my_list = my_str.split()
# my_list is ['wlo1', 'Link', 'encap:Ethernet', 'HWaddr', 'b4:6d:83:77:85:f3']


# We concatenate the first list element, '!' and the last list element
interface_mac = my_list[0] + '!' + my_list[-1]
print(interface_mac)  # => wlo1!b4:6d:83:77:85:f3

# List with duplicates
years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []

# Adding only unique elements from years in years_unique
[years_unique.append(item) for item in years if item not in years_unique]

print(years_unique)  # => [2010, 2011, 2012]

# List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom']

# List comprehension that constructs a list of palindromes from names list
palindromes = [items for items in words if items.lower() == items[::-1].lower()]

print(palindromes)  # => ['Anna', 'Civic', 'Level', 'Mom']


def remove_from_list(my_list, item):
    """
    Function that removes an item from a list.
    """
    while (item in my_list):  # check if the element belongs to the list
        my_list.remove(item)  # remove THE FIRST occurrence of the element


list1 = [1, 2, 1, 1, 1, 1, 3]

# Calling the function and remove 1 from the list
remove_from_list(list1, 1)

print(list1)  # => [2, 3]

countries = ['USA', 'UK', 'France', 'Romania', 'France', 'Germany', 'USA', 'Canada', 'India', 'UK']

# Removing duplicates from list by transforming it to a set and then back to a list
countries = list(set(countries))
countries.sort()  # Sorting the list in place

print(countries)  # => ['Canada', 'France', 'Germany', 'India', 'Romania', 'UK', 'USA']
