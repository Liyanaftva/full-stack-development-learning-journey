'''fetch input from user, if it is a number store it in the list, else do not store, using built-in function'''
l=[]
limit=int(input("Enter the length of the list:"))
for i in range(limit):
    n=input("Enter the data:")                        
    if n.isdecimal()==True:
        l.append(n)
print(l)
# ======================================================================================
'''Find the largest number in a list, fetch the list from the user'''
l=[]
large=l[0]
limit=int(input("Enter the length of the list:"))
for i in range(limit):
    n=int(input("Enter the data:"))
    l.append(n)
for i in l:
    if i>large:
        large=i
print(large)
# ======================================================================================
'''Fetch word data list from a user and ask user to give the position of the data to be reversed, with and without using built-in function'''
l=[]
rev=''
limit=int(input("Enter the length of the list:"))
for i in range(limit):
    n=input("Enter the data:")
    l.append(n)
print(l)
fetch=int(input("Enter the position of data to be reversed:"))
if fetch<=limit:
    s=l[fetch-1]
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)
# ======================================================================================
'''Fecth a list from the user and replace the even numbers with zeroes'''
l=[]
limit=int(input("Enter the length of the list:"))
for i in range(limit):
    n=int(input("Enter the data:"))
    l.append(n)
for i in range(len(l)):
    if l[i]%2==0:
        l[i]=0
print(l)    
# ======================================================================================
'''Fecth positive, negative and zeroes, and ouput the count of each in a list'''
l=[]
p_count=0
n_count=0
z_count=0
limit=int(input("Enter the length of the list:"))
for i in range(limit):
    n=int(input("Enter the data:"))
    l.append(n)
for i in l:
    if i>0:
        p_count+=1
    elif i==0:
        z_count+=1
    else:
        n_count+=1
print(f"Positive = {p_count}, Negative = {n_count}, Zeroes = {z_count}")
# ======================================================================================
'''Sum of two lists'''
l1=[2,3,5,7]
l2=[6,3,8,4]
l3=[]
for i in range(len(l1)):
    sum=l1[i]+l2[i] 
    l3.append(sum)
print(l3)
# ======================================================================================
'''Prime numbers in a list'''
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
prime=[]
for i in l:
    count=0
    j=1
    while j<=i:
        if i%j==0:                                       
            count+=1
        j+=1
    if count==2:
        prime.append(i)
print(prime)
# ======================================================================================
'''Replace negative numbers with positiVe numbers'''
l=[1,3,-4,5,-63,-4,2,-76,9,9,-5]
for i in range(len(l)):
    if l[i]<0:
        l[i]=-l[i]
print(l)     
# ======================================================================================
'''Factorial of the numbers in a list'''
l=[1,2,3,4,5]
factorial=[]
for i in l:
    fact=1
    for j in range(1,i+1):
        fact*=j
    factorial.append(fact)
print(factorial)
# ======================================================================================
'''count the repetitive numbers in a list'''
l=[2,1,4,6,8,9,4,3,6,8,84,3,7,8,6,4,2,5,774,2,2,25,7,23]
store=[]
for i in l:
    if i not in store:
        count=0
        for j in l:
            if i==j:
                count+=1
        print(f"{i} = {count}")
    store.append(i)
# ======================================================================================
'''store strings in a list, count the words having starting and ending letters same'''
l=['aba','farah','nanaa','lol','girirsh','nunan']
store=[]
for i in l:
    new=''
    new+=i
    length=len(i)
    if i[0]==new[length-1]:
        store.append(i)
print(store)
# ======================================================================================