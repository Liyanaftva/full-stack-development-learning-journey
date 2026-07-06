# ======================================================================================
'''TUPLE DATA TYPE'''
# ======================================================================================
t=(3.14,)
print(type(t))
v=()
print(type(v))
b=tuple()
print(type(b))
# ======================================================================================
'''SET DATA TYPE'''
# It is an unordered collection of items
# represented by {}, every elemeny is unique and must be immutable
# it is not indexed, we cannot use index value to get an item
# duplicate values will not be allowed in set
# set stores only immutable data types and does not store mutable data types like list
# set data type is mutabel since we can add and remove items, but the datas stored in set must be immutable
# it can be used to perform set operations like union, intersection, symmetric difference, etc
# we can add a single element using add() method and multiple elements using update() method
# ======================================================================================
name={'a','b','c',1,2,3,4,5,6,1,2,3,4,2,1,2,3,1,[1,2,3]}
print(type(name))
print(name)
print(name[3])
# ======================================================================================
s={}        # dictionary type
print(type(s))
s=set()
print(type(s))
# ======================================================================================
name={'a','b','c',1,2,3,4,5,6,1,2,3,4,2,1,2,3,1,(1,2,3)}        # tuple is immutable so we can add tuple
print(name)
# ======================================================================================
name={'a','b','c',1,2,3,4,5,6,1,2,3,4,2,1,2,3,1,(1,2,3)}
for i in name:            # we cannot be sure of the order, thus "if" is of no great use
    print(i)
# ======================================================================================
print(dir(set))
'''['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection',
    'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
    'symmetric_difference', 'symmetric_difference_update', 'union', 'update']'''
# ======================================================================================
'''add()'''
s={1,2,3}
s.add(4)        # the position is not defined thus, the items will store in random positions
s.add('a')
s.add(1.34)
s.add('g')
s.add(6)
print(s)
# ======================================================================================
'''clear()'''
s={1,2,3}
s.clear()           # prints set() instead of {}
print(s)
# ======================================================================================
'''copy()'''
s={1,2,3}
s1=s.copy()
print(s)
print(s1)
# ======================================================================================
'''difference()'''
s={1,2,3,5,6}       # s-s1 , i.e, common elements from s and s1 is removed and print the remaining elements from s
s1={3,4,5,6}
c=s.difference(s1)
print(c)
print(s)
# ======================================================================================
a={1,2,3,4,5,6,7}
b={1,2,3}
c={6,7}
print(a.difference(b,c))
# ======================================================================================
a={1,2,3,4,5,6,7}
b={1,2,3}
print(a-b)        # instead of difference "-" symbol can be used
# ======================================================================================
'''difference_update()'''
a={1,2,3,4}
b={3,4,5}
a.difference_update(b)        # updation happened in the variable "a" itself
print(a)
# ======================================================================================
a={1,2,3,4,5,6,7,8,9}
b={3,4,5}
c={4,5,6,7}
a.difference_update(b,c)        
print(a)
# ======================================================================================
'''discard()'''
a={1,2,3,4,5,6,7,8,9}
a.discard(2)        # remove an element from the set if it is present
print(a)
# ======================================================================================
a={1,2,3,4,5,6,7,8,9}
a.discard(11)
print(a)
# ======================================================================================
'''intersection()'''
a={1,2,3,4}
b={3,4,5,6,7,8}
c=a.intersection(b)
print(c)
# ======================================================================================
'''intersection_update()'''
a={1,2,3,4}
b={3,4,5,6,7,8}
a.intersection_update(b)
print(a)
# ======================================================================================
'''union()'''
a={1,2,3,4}
b={3,4,5,6,7,8}
c=a.union(b)
print(c)
# ======================================================================================
a={1,2,3,4}
b={3,4,5,6,7,8}
d=a|b           # instead of union() we can use "|" symbol
print(d)
# ======================================================================================
a = {1, 2}
result = a.union([3, 2, 4],(5, 6),"hi")          # takes each data, as it iterates through list, tuple and string
print(result)
# ======================================================================================
'''isdisjoint()'''
a = {1, 2, 3, 4}
b = {7, 6, 5, 9}
print(a.isdisjoint(b))
# ======================================================================================
a = {1, 2, 3, 4, 7}
b = {7, 6, 5, 9}
print(a.isdisjoint(b))
# ======================================================================================
'''issubset()'''
a = {1, 2, 3, 4, 7}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.issubset(b))
# ======================================================================================
a = {1, 2, 3, 4, 7, 0}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.issubset(b))
# ======================================================================================
'''issuperset()'''
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 20}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.issuperset(b))
# ======================================================================================
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 20}
b = {1, 2, 3, 4, 5, 6, 7, 19, 8, 9}
print(a.issuperset(b))
# ======================================================================================
'''remove()'''
s = {1, 2, 3}
s.remove(2)
print(s)
# ======================================================================================
'''symmetric_difference()'''
a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 7, 9, 5}
result = a.symmetric_difference(b)
print(result)
# ======================================================================================
'''symmetric_difference_update()'''
a = {1, 2, 3, 4, 5, 6}
b = {2, 3, 7, 9, 5}
a.symmetric_difference_update(b)
print(a)
# ======================================================================================
'''update()'''
s = {1, 2, 3, 4}
s.update("help",[4, 5, 6, 7])
print(s)
# ======================================================================================
a={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}
print(odd.issubset(a))
print(even.issubset(a))
print(a.issuperset(odd))
print(a.issuperset(even))
# ======================================================================================
a = {1, 2, 3, 4}
b = {1, 2, 3, 4}
print(a==b)         # value is same
print(a is b)       # memory location si different
# ======================================================================================
a = {10, 20, 30, 40}
print(a*3)          # unsupported
# ======================================================================================
'''fetching set from the user'''
s=set()
limit=int(input("Enter the limit:"))
for i in range(limit):
    a=input("Enter the data:")
    s.add(a)
print(s)
# ======================================================================================