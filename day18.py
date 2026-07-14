# ======================================================================================

'''DICTIONARY DATA TYPE'''

# ======================================================================================

'''popitem'''       # pop should have atleast one argument whereas popitem takes no argument
data = {"name":"Miya", 
        "age":23, 
        "place":"Calicut",
        "Pno":"9544345675"}
data.popitem()
print(data)             # {'name': 'Miya', 'age': 23, 'place': 'Calicut'}
# ======================================================================================

'''setdefault'''
d = {'a':1}                         # if present, it doesn't overwrite, else, it sets the item in dictionary
print(d.setdefault('a', 100))       # 1
print(d)                            # {'a': 1}
# ======================================================================================

d = {'k':1}
print(d.setdefault('a', 100))       # 100
print(d)                            # {'k': 1, 'a': 100}
# ======================================================================================

d = {'k':1}
print(d.setdefault('a'))            # None
print(d)                            # {'k': 1, 'a': None}
# ======================================================================================

'''update'''
dic = {'name':'Aswathi',
       'age':30,
       'place':'kollam'}
print(dic)                          # {'name': 'Aswathi', 'age': 30, 'place': 'kollam'}
dic['age'] = 88
dic['dept'] = 'communication'
print(dic)                          # {'name': 'Aswathi', 'age': 88, 'place': 'kollam', 'dept': 'communication'}
# ======================================================================================

dic1 = {'name':'Aswathi',
       'age':30,
       'place':'kollam'}
dic2 = {'name':'alice',
        'age':20,
        'salary':20000}
dic1.update(dic2)
print(dic1)                         # {'name': 'alice', 'age': 20, 'place': 'kollam', 'salary': 20000}
# ======================================================================================

dic1 = {'name':'Aswathi',
       'age':30,
       'place':'kollam'}
dic1.update(name = 'Alice')
print(dic1)                         # {'name': 'Alice', 'age': 30, 'place': 'kollam'}
# ======================================================================================

dic1 = {'name':'Aswathi',
       'age':30,
       'place':'kollam'}
dic1.update(phno = 97437762379, dep='science')
print(dic1)                         # {'name': 'Aswathi', 'age': 30, 'place': 'kollam', 'phno': 97437762379, 'dep': 'science'}
# ======================================================================================

my_dict = {'fruit':'pineapple'}
new_items = [('color','yellow'), ('taste','sweet')]
my_dict.update(new_items)
print(my_dict)                      # {'fruit': 'pineapple', 'color': 'yellow', 'taste': 'sweet'}
# ======================================================================================

'''DICTIONARY COMPREHENSION'''
# It is similar to list comprehension
# it uses single line
# expression followed by for loop and if needed if clause
# syntax: variable = {key_expression: value_expression for item in iterable if condition}
# ======================================================================================

'''using a traditional for loop, create a dictionary of numbers and their squares'''
numbers = [1, 2, 3, 4, 5]
squares = {}
for i in numbers:
    squares[i] = i*i
print(squares)                  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ======================================================================================

'''using dictionary comprehension, create a dictionary of numbers and their squares'''
numbers = [1, 2, 3, 4, 5]
squares = {x : x*x for x in numbers}
print(squares)                  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ======================================================================================

'''create a dictionary of even numbers and their cubes'''
even_cubes = {x : x**3  for x in range(1,51) if x % 2 == 0}
print(even_cubes)               # {2: 8, 4: 64, 6: 216, 8: 512, 10: 1000, 12: 1728, 14: 2744, 16: 4096, 18: 5832, 20: 8000, 22: 10648, 24: 13824, 26: 17576, 28: 21952, 30: 27000, 32: 32768, 34: 39304, 36: 46656, 38: 54872, 40: 64000, 42: 74088, 44: 85184, 46: 97336, 48: 110592, 50: 125000}
# ======================================================================================

'''create a dictionary of characters and their ascii value from a given string'''
s = 'programming'
ascii = {x : ord(x) for x in s}
print(ascii)                    # {'p': 112, 'r': 114, 'o': 111, 'g': 103, 'a': 97, 'm': 109, 'i': 105, 'n': 110}
# ======================================================================================

'''swap key and values in a a dictionary'''
org_dict = {'a':1, 'b':2, 'c':3, 'd':4}
swap = {j : i for i,j in org_dict.items()}
print(swap)
# ======================================================================================

'''count number of students who gets mark more than 50'''
std_mark = {'arun' : 23, 'miya' : 54, 'olive' : 64, 'ginger' : 34, 'megha' : 58}
count = 0
for i in std_mark:
    if std_mark.get(i)>50:
        count+=1
print(count)
# ======================================================================================

'''update the mark of a given student'''
std_mark = {'arun' : 23, 'miya' : 54, 'olive' : 64, 'ginger' : 34, 'megha' : 58}
print(std_mark)
name = input("Enter the name of the student whose mark is to be changed:")
mark = int(input("Enter the mark to be given:"))
for i in std_mark:
    if i == name:
        std_mark[name] = mark
print(std_mark)
# ======================================================================================

'''NESTED DICTIONARY'''

# ======================================================================================

{"liyana@gmail.com" : {"name" : "liyana", "age" : 21},
 "miya@gmail.com" : {"name" : "miya", "age" : 24},
 "diya@gmail.com" : {"name" : "diya", "age" : 24}}
main = {}
sub = {}
email = input("Enter you email:")
name = input("Enter your name:")
age = int(input("Enter your age:"))
sub["name"] = name
sub["age"] = age
main[email] = sub
print(main)
# ======================================================================================

main = {}
limit = int(input("Enter the number of items you want in the dictionary:"))
for i in range(limit):
    sub = {}
    email = input("Enter you email:")
    name = input("Enter your name:")
    age = int(input("Enter your age:"))
    sub["name"] = name
    sub["age"] = age
    main[email] = sub
print(main)         # {'liya@gmail.com': {'name': 'liya', 'age': 21}, 'miya@gmail.com': {'name': 'miya', 'age': 23}, 'diya@gmail.com': {'name': 'diya', 'age': 24}}
for i,j in main.items():
    print(i)
    print(j)
''' OUTPUT:
liya@gmail.com
{'name': 'liya', 'age': 21}
miya@gmail.com
{'name': 'miya', 'age': 23}
diya@gmail.com
{'name': 'diya', 'age': 24} '''
# ======================================================================================

'''Delete a list of keys from a dictionary
sample_dict={"name":'Kelly","age":20,"salary":10000,"city":"Kochi"}
keys = ['name","salary"]'''
sample_dict={"name" : "Kelly","age" : 20, "salary" : 10000, "city" : "Kochi"}
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)                  # {'age': 20, 'city': 'Kochi'}
# ======================================================================================