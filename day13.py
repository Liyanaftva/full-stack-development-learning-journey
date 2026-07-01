# ======================================================================================

'''SEQUENCE DATA TYPES'''

# ======================================================================================
'''LIST DATA TYPE'''
list1=[]  # enclosed in square brackets
list2=[1,2,3,4,'a','b','c',1.34,True]  # can store multiple data types
list3=[1,2,2,3,3,'a','b','a',1,3]   # duplicates are allowed, it is ordered, have index values, both positive and negative index, it is mutable
# ======================================================================================
'''LIST BUILT IN METHODS'''
print(dir(list))
'''['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']'''
# ======================================================================================
list3=[1,2,2,3,3,'a','b','a',1,3]
print(list3)
list3.append(19)   # values are added to end of the list
print(list3)
list3.append(29)
print(list3)
list3.append("a")
print(list3)
# ======================================================================================
list2=[1,2,3,4,'a','b','c',1.34,True]
print(list2) 
list2.clear()  # clear all the values in a list
print(list2)
# ======================================================================================
a=[1,2,3,4,5]
print(a)
b=a.copy()   # copies the values of a variable from one variable to the other
print(b)     # any additional operation performed on original doesn't affect copy
c=a          # since it is assigned, any changes in original affect the asssigned variable
print(c)
print(id(a))
print(id(b))
print(id(c))
a.append("k")
print(a)
print(b) 
print(c)
# ======================================================================================
a=[1,2,4345,56,7,7,8,7]
print(a.count(7))
print(a.count(4))
# ======================================================================================
a=[1,2,3,4,5,6,7]
b=[34,67,89]
a.append(b)   # append inserts or adds only one element
print(a)
c=[2,3,4]
b.extend(c)   # extend inserts or adds every elements seperately
print(b)
# ======================================================================================
l=[1,2,3,"a","b",60,2.45]
print(l.index("a"))   # returns index position
print(l.index(5))     # if data not present, returns error
# ======================================================================================
l=[1,2,3,4,5,6,7,8]
l.insert(5,100)    # used to insert value in a specific position and shifts the position to the right, no data loss, but length increased
print(l)
# ======================================================================================
l=[1,2,3,4,5,6]
l[4]=200    # it overwrites the data, thus data loss occurs
print(l)
# ======================================================================================
l=[1,23,4,34,7,7,8,3,5]
print(l.pop(3))    # removes the value in the index position, and returns the list after removing that value
print(l)           # here we specify the indexx position
# ======================================================================================
l=[1,23,4,34,7,7,8,3,5]
l.pop()   # pops the end value
print(l)
# ======================================================================================
l=[1,2,3,4,5,6,2,3]
l.remove(3)     # removes the first occurence of 3
print(l)
# ======================================================================================
l=[1,2,3,4,5]
l.reverse()     # reverse the list
print(l)
# ======================================================================================
l=[23,4,12,6,1,4,6,3,667,3456,4,343234,345,34]
l.sort()    # sorts in ascending order by default
print(l)
# ======================================================================================
l=[23,4,12,6,1,4,6,3,667,3456,4,343234,345,34]
l.sort(reverse=True)
print(l)
# ======================================================================================
l=[23,4,12,6,1,4,6,3,667,3456,4,343234,345,34]
l.sort()
l.reverse()
print(l)
# ======================================================================================
l=[23,4,12,6,1,4,6,3,667,3456,4,343234,345,34,"a","n"]
l.sort()
print(l)
# ======================================================================================
l=["d","g","s","a","e","t","l","o","n","b"]
l.sort()
print(l)
# ======================================================================================
l=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    num=int(input("Enter the number:"))
    l.append(num)
print(l)
for i in l:
    print(i)
# ======================================================================================
'''fetch a number list and print numbers above 50'''
l=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    num=int(input("Enter the number:"))
    l.append(num)
for i in l:
    if i>50:
        print(i)
# ======================================================================================
'''write a program to calculate the sum of list of the numbers'''
l=[]
sum=0
limit=int(input("Enter the limit:"))
for i in range(limit):
    num=int(input("Enter the number:"))
    l.append(num)
for i in l:
    sum+=i
print("sum =",sum)
# ======================================================================================
'''print the first and last numbers from a list'''
l=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    num=int(input("Enter the number:"))
    l.append(num)
print("first number is ",l[0],"and last number is",l[limit-1])
# ======================================================================================
'''merge two lists with and without built-in methods'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
l1.extend(l2)
print(l1)
# ======================================================================================
l1=[1,2,3,4,5]
l2=[6,7,8,9,0]
print(l1+l2)
# ======================================================================================
'''fetch datas for a list from the user and fetch an additional data and check whether the data is present in the list or not'''
l=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    num=int(input("Enter the number:"))
    l.append(num)
search=int(input("Enter the value to be found:"))
for i in l:
    if i==search:
        print(f"The value {i} is found at index position {l.index(i)}")
# ======================================================================================
'''covert all the "b" in a list to "k"'''
l=["a","b","d","b","s","e","t","r","b","l"]
for i in range(len(l)):
    if l[i]=="b":
        l[i]="k"
print(l)
# ======================================================================================
'''if zeroes are present in a list, shift the position of zeroes to the end of the list'''
l=[1,2,0,3,4,5,6,3,4,0,5,0]
nz=[]
z=[]
for i in l:
    if i!=0:
        nz.append(i)
    else:
        z.append(i)
print(nz+z)
# ======================================================================================