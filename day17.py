'''TUPLE FUNCTIONS'''
# ======================================================================================

print(dir(tuple))
'''count(),index()'''
n=(1,2,3,4,5,2,3,4,5,2,23,4,2,3,4,6,7,6,7,8,9)
print(n.count(2))		# 4
print(n.count(20))		# count of non-existent element will be 0
print(n.index(3))		# first elements index
print(n.index(20))		# error
# ======================================================================================

'''DICTIONARY DATA TYPE'''
# It is a  sequence data type
# It is ordered, before 3.6 it was unordered
# represented by {}, every data is stored in key-value pairs
# it is also known as mapping data type
# It is mutable
# we fetch or get value by key and not index, but it is indexed
# one key-value pair is named as an item
# the first part in the item is key and the second part is the value
# key must be unique, but values can be duplicate, otherwise there will be data loss
# ======================================================================================

dict1 = {"name":"Liyana", "age":45}
print(dict1)
dict2 = {"name":"Liyana", "age":21, "name":"Leya"}
print(dict2)        # value gets overwritted
dict3 = {"name":"Liyana", "age":21, "name1":"Leya"}
print(dict3)
dict4 = {"name":"Liyana", "age":21, "name1":"Leya", "name2":"Miya"}
print(dict4)
# ======================================================================================

dict1 = {"name":"Liyana", "age":45}
print(dict1[2])         # we can't get value using index, only key can be used to get the value
print(dict1["name"])    # Liyana
# ======================================================================================

'''creation of dictionary'''
data = {}
data["name"] = "Liyana"
data["age"] = 21
data["place"] = "Wayanad"
print(data)           # {'name': 'Liyana', 'age': 21, 'place': 'Wayanad'}
data["name"] = "Diya"
print(data)           # {'name': 'Diya', 'age': 21, 'place': 'Wayanad'}
# ======================================================================================

'''Fetching dictionary from the user'''
entry = {}
limit = int(input("Enter the limit of the data to be entered:"))
for i in range(limit):
    key = input("Enter the key:")
    value = input("Enter the value:")
    entry[key] = value
print(entry)
# ======================================================================================

name_age = {}
name = input("Enter the name:")
age = int(input("Enter the age:"))
name_age[name] = age
print(name_age)             # {'anu': 32}
# ======================================================================================

'''Functions of Dictionary'''
print(dir(dict))
'''['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']'''
# ======================================================================================

'''clear'''
data = {'name': 'Diya', 'age': 21, 'place': 'Wayanad'}
print(data)         # {'name': 'Diya', 'age': 21, 'place': 'Wayanad'}
data.clear()
print(data)         # {}
# ======================================================================================

'''copy'''
data = {'name': 'Diya', 'age': 21, 'place': 'Wayanad'}
copy_data = data.copy()
print(copy_data)       # {'name': 'Diya', 'age': 21, 'place': 'Wayanad'}
# ======================================================================================

'''fromkeys'''
data = {}
data['a'] = 1
data['b'] = 1
data['c'] = 1
print(data)                                 # {'a': 1, 'b': 1, 'c': 1}, not applicable if there are lots of keys
# ======================================================================================

fromkey_data = {}
keys = ['a', 'b', 'c', 'd']
fromkey_data = dict.fromkeys(keys, 1)       # assigning same value '1' to every keys in 'keys' variable
print(fromkey_data)                         # {'a': 1, 'b': 1, 'c': 1, 'd': 1}
# ======================================================================================

'''get'''
d = {'a':1, 'b':2}
print(d.get('a'))                              # 1 (first it maps the key in the dictionary, and find it's value)
print(d.get('k'))                              # None
# ======================================================================================

'''items'''
data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut"}
for i in data:
    print(i)                                    # we'll only get keys
    print(data[i])                              # we'll get values only
# ======================================================================================

data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut"}
for i, j in data.items():
    print(i, j)                                 # we'll get both keys and values
# ======================================================================================

'''keys'''
data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut"}
for i in data.keys():
    print(i)                                      # we'll get keys only
# ======================================================================================

'''values'''
data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut"}
for i in data.values():
    print(i)                                        # we'll get only values
# ======================================================================================

'''pop'''
data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut"}
data.pop("age")
print(data)                                           # {'name': 'Miya', 'place': 'Calicut'}
# ======================================================================================

'''Convert two lists into a dictionary.'''
number_digit = [10, 20, 30, 40]
number_alphabet = ['Ten', 'Twenty', 'Thirty', 'Fourty']
numbers = {}
for i in range(len(number_digit)):
    numbers[number_digit[i]]=number_alphabet[i]
print(numbers)          # {10: 'Ten', 20: 'Twenty', 30: 'Thirty', 40: 'Fourty'}
# ======================================================================================

'''Fetch keys and values from the user and create a dictionary.'''
name_n_place = {}
limit = int(input("Enter the limit of the data to be entered:"))
for i in range(limit):
    name = input("Enter the name:")
    place = input("Enter the place:")
    name_n_place[name] = place
print(name_n_place)       # {'josh': 'new york', 'killian': 'russia', 'aiden': 'london', 'dmitri': 'italy'}
# ======================================================================================

'''Find the highest mark in a dictionary created from user input.'''
data = {}
limit = int(input("Enter the limit of the data to be entered:"))
for i in range(limit):
    name = input("Enter the name:")
    mark = int(input("Enter the mark:"))
    data[name] = mark
largest = 0
for i in data.values():
    if i > largest:
        largest = i
print("largest mark =", largest)            # largest mark = 89
# ======================================================================================

'''Fetch a dictionary from the user and print its keys and values.'''
data = {}
limit = int(input("Enter the limit of the data to be entered:"))
for i in range(limit):
    name = input("Enter the name:")
    mark = int(input("Enter the mark:"))
    data[name] = mark
for i in data.items():
    print(i)                                 # ('leon', 23) ('kiran', 56) ('arya', 34)
# ======================================================================================
