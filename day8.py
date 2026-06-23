# """SELF PRACTICE QUESTIONS, NOT TAUGHT AT ACADEMY"""
 
'''Question 7: Palindrome Check
Problem Statement: Determine whether the string is a palindrome.
Sample Input
madam
Sample Output
True'''

s='madam'
l=len(s)
i=l-1
rev=''
while i>=0:
    rev+=s[i]
    i-=1
if rev==s:
    print(True)
else:
    print(False)
# ======================================================================================
'''Question 8: Count Vowels
Problem Statement: Count the number of vowels in the string.
Sample Input
education
Sample Output
5'''

s="education"
l=len(s)
i=0
count=0
while i<l:
    if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I'or s[i]=='O' or s[i]=='U':
        count+=1
    i+=1
print(count)
# ========================================================================================
'''Question 9: Count Consonants
Problem Statement: Count the number of consonants in the string.
Sample Input
education
Sample Output
4'''

s="education"
l=len(s)
i=0
count=0
while i<l:
    if s[i] not in {'a','e','i','o','u','A','E','I','O','U'}:
        count+=1
    i+=1
print(count)
# =========================================================================================
'''Question 10: Convert to Uppercase
Problem Statement: Convert all characters to uppercase.
Sample Input
hello
Sample Output
HELLO'''

s="hello"
print(s.upper())
# ==========================================================================================
'''Question 11: Convert to Lowercase
Problem Statement: Convert all characters to lowercase.
Sample Input
HELLO
Sample Output
hello'''

s="HELLO"
print(s.lower())
# ==========================================================================================
'''Question 12: Toggle Case
Problem Statement: Toggle the case of every character.
Sample Input
HeLLo
Sample Output
hEllO'''

s="HeLLo"
print(s.swapcase())
# ==========================================================================================
'''Question 13: Remove Spaces
Problem Statement: Remove all spaces from the string.
Sample Input
I love Python
Sample Output
IlovePython'''

s="I love Python"
new=''
i=0
l=len(s)
while i<=l-1:
    if s[i]!=" ":
        new+=s[i]
    i+=1
print(new)
# ============================================================================================
'''Question 14: Count Words
Problem Statement: Count the number of words in a sentence.
Sample Input
I love Python
Sample Output
3'''

s="I love Python"
count=1
l=len(s)
i=0
while i<l-1:
    if s[i]==" ":
        count+=1
    i+=1
print(count)
# ============================================================================================
'''Question 15: Reverse Word Order
Problem Statement: Reverse the order of words in a sentence.
Sample Input
I love Python
Sample Output
Python love I'''

s="I love Python"
words=s.split()
l=len(words)
i=l-1
while i>=0:
    print(words[i],end=' ')
    i-=1
# ============================================================================================

# '''CLASS PRACTICE'''

'''break jumping statement'''
# ===========================================================================================
num=1
while num<=10:
    if num==7:
        break
    else:
        print(num)
    num+=1
# ============================================================================================
num=1
while num<=10:
    if num==7:
        break    # the while and else part won't work
    else:
        print(num)
    num+=1
else:
    print("completed")
print("exiting the while else")
# ============================================================================================
'''continue jumping statement'''
# ===========================================================================================
num=1
while num<=10:
    if num==7:
        continue    #statements under continue won't work, thus num+=1 won't work
    else:
        print(num)
    num+=1
# ===========================================================================================
num=0
while num<10:
    num+=1
    if num==7:
        continue
    else:
        print(num)
# ===========================================================================================
'''pass jumping statement(it works in anywhere, while, for, function, etc)'''
# ===========================================================================================
num=0
while num<5:
    pass    # we only need to write the code later and is used to avoid syntax error
    num+=1
print("hii")
# ===========================================================================================
def show():
    pass    # function is yet to study
print("hello")
# ===========================================================================================
'''while true statement'''
# ===========================================================================================
'''get number from the user, should not print 50'''
while True:   # if we need to ask the statement infinitely, while true is used.
    num=int(input("Enter the number:"))   
    if num==50:
        break
    print(num)
# ===========================================================================================
while 1==1:   # either give true or any true condition
    num=int(input("Enter the number:"))   
    if num==50:
        break
    print(num)
# ===========================================================================================
'''Number guessing game'''
while True:   
    num=int(input("Enter the number:"))   
    if num==67:
        print("Correct")
        break
    else:
        print("Incorrect")
# ===========================================================================================