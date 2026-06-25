'''reverse of string using for loop'''
s="liyana"
rev=''
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)
# =========================================================================================================
'''length of a string using for loop'''
s="english"
count=0
for i in s:
    count+=1
print(count)
# =========================================================================================================
'''how many words in a sentence using for loop'''
s="i love python"
count=1
new=''
for i in s:
    if i!=" ":
        new+=i
    else:
        if new!=" ":
            count+=1
            new=' '
print(count)
# =========================================================================================================
'''common elements in 2 strings using for loop'''
s1="english"
s2="manglish"
for i in s1:
    for j in s2:
        if i==j:
            print(i)
# =========================================================================================================
'''count of repeating characters in a string'''
s="malayalam"
store=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>1:
        if i not in store:
                store+=i+" = "+str(count)+" "
print(store,"are the repeating charcters and its count in the string",s)    
# =========================================================================================================
'''print the repeating character in a string'''
s="malayalam"
store=""
for i in s:
    count=0
    for j in s:
        if i==j:
            count+=1
    if count>1:
        if i not in store:
                store+=i+" "
print(store,"are the repeating charcters in the string",s)    
# =========================================================================================================
'''Print Numbers from 1 to 20
Use range() and a for loop.'''
for i in range(21):
    print(i)
# =======================================================================================================
'''common elements in 2 strings using for loop using membership operator'''
s1="english"
s2="manglish"
store=""
for i in s1:
    if i in s2:
        if i not in store:
            store+=i+" "
print(store)
# =======================================================================================================
'''Print Even Numbers from 1 to 50
Use range().'''
for i in range(1,51):
    if i%2==0:
        print(i)
# =======================================================================================================
'''Digit sum using for loop'''
num=2345
sum=0
for i in str(num):
    sum+=int(i)
print(sum)
# =======================================================================================================
'''multiplication table using for loop'''
num=6
mul=1
for i in range(1,11):
    mul=i*num
    print(f"{i} x {num} = {mul}")
# =======================================================================================================
'''check whether a string is palindrome or not using for loop'''
s=input("Enter the string:")
rev=''
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
if rev==s:
    print(f"The string {s} is palindrome")
else:
    print(f"The string {s} is not palindrome")
# =======================================================================================================
s=input("Enter the string:")
rev=''
for i in range(0,len(s),1):
    rev=s[i]+rev
if rev==s:
    print(f"The string {s} is palindrome")
else:
    print(f"The string {s} is not palindrome")
# =======================================================================================================
'''Print Odd Numbers from 1 to 50
Use range().'''
for i in range(1,11):
    if i%2!=0:
        print(i)
# =======================================================================================================
'''Find Sum of Numbers from 1 to 100
Use a for loop.'''
sum=0
for i in range(1,101):
    sum+=i
print(sum)
# =======================================================================================================
'''Find Factorial of a Number
Take a number from the user and calculate its factorial.'''
n=int(input("Enter the number:"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# =======================================================================================================