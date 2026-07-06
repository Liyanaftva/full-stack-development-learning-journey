'''Create a set named fruits with elements: "apple", "banana", "cherry". Print it.'''
fruits = {"apple", "banana", "cherry"}
print(fruits)                                   # {'cherry', 'banana', 'apple'}
# ======================================================================================
'''Add "orange" to the fruits set.'''
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)                                  # {'orange', 'apple', 'banana', 'cherry'}
# ======================================================================================
'''Remove "banana" from the set using both .remove() and .discard() — see the difference.'''
fruits = {'orange', 'apple', 'banana', 'cherry'}
fruits.remove("banana")                        # {'apple', 'orange', 'cherry'}
fruits.discard("banana")                       # {'apple', 'orange', 'cherry'}
print(fruits)
# ======================================================================================
'''Check if "apple" is present in the set.'''
fruits = {'apple', 'orange', 'cherry'}
if 'apple' in fruits:                          # 'apple' is present
    print("'apple' is present")
else:
    print("'apple' is not present")
# ======================================================================================
'''Find the length of the set.'''
fruits = {'apple', 'orange', 'cherry'}
print(len(fruits))                             # 3
# ======================================================================================
'''Create two sets a = {1,2,3,4} and b = {3,4,5,6}. Find their union.'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.union(b)
print(result)                                  # {1, 2, 3, 4, 5, 6}
# ======================================================================================
'''Find the intersection of the two sets above.'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.intersection(b)
print(result)                                  # {3, 4}
# ======================================================================================
'''Find the difference between the two sets (a - b and b - a).'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result1 = a.difference(b)
result2 = b.difference(a)
print(result1)                                 # {1, 2}
print(result2)                                 # {5, 6}
# ======================================================================================
'''Find the symmetric difference of sets a and b.'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
result = a.symmetric_difference(b)
print(result)                                  # {1, 2, 5, 6}
# ======================================================================================
'''Convert a list [1,2,2,3,4,4,5] into a set to remove duplicates.'''
list_original = [1, 2, 2, 3, 4, 4, 5]
list_to_set = set(list_original)
list_converted = list(list_to_set)
print(list_converted)                          # [1, 2, 3, 4, 5]
# ======================================================================================
'''Given set1 = {10, 20, 30} and set2 = {20, 40, 50}, update set1 with all elements from set2.'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.update(set2)
print(set1)                                   # {50, 20, 40, 10, 30}
# ======================================================================================
'''Check whether set1 is a subset or superset of set2'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}
if set1.issubset(set2):
    print("set1 is a subset of set2")         # set1 is neither subset nor superset of set2
elif set1.issuperset(set2):
    print("set1 is a superset of set2")
else:
    print("set1 is neither subset nor superset of set2")
# ======================================================================================
'''Remove all elements from a set using .clear().'''
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.clear()
print(set1)                                   # set()
# ======================================================================================
'''Create a frozen set from list [1,2,3,4]. Try adding a new element—observe the error.'''
list_original = [1, 2, 3, 4]
set_frozen = frozenset(list_original)         # frozenset({1, 2, 3, 4})
set_frozen.add(7)                             # 'frozenset' object has no attribute 'add'
print(set_frozen)
# ======================================================================================
