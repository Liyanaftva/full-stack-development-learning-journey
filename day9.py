# =========================================================================================================

"""SELF PRACTICE QUESTIONS, NOT TAUGHT AT ACADEMY"""

# =========================================================================================================

'''Question 16: Longest Word
Problem Statement: Find the longest word in a sentence.
Sample Input
I love programming
Sample Output
programming'''

s="I love programming"
word=s.split()
longest=word[0]
i=0
while i<len(word):
    if len(word[i])>len(longest):
        longest=word[i]
    i+=1
print(longest)
# =========================================================================================================

'''CLASS PRACTICE'''

# =========================================================================================================

'''fetch an option from the user, +,-,*./ and exit, when user selects the exit option, the loop should exit.'''
print('''***THE CHOICES***
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      5. Exit''')
while True:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    choice=int(input("Enter the choice:"))
    if choice==1:
        print("Sum is",num1+num2)
    elif choice==2:
        print("Difference is",num1-num2)
    elif choice==3:
        print("Product is",num1*num2)
    elif choice==4:
        print("Quotient is",num1/num2)
    elif choice==5:
        break
    else:
        print("Invalid Choice")
# =========================================================================================================
'''Fetch number from user until the user enters a negative number, if the user enters the negative number, print the sum and break from the loop'''
sum=0
while True:
    a=int(input("Enter the number:"))
    if a>=0:
        sum+=a
    else:
        print("sum =",sum)
        break
# =========================================================================================================
'''Fetch names from user until the user enters a stop string, if the user enters the stop, print the names and break from the loop'''
while True:
    s=input("Enter the name:")
    if s=="stop":
        print("Completed")
        break 
    print(s)
# =========================================================================================================
name=''
while True:
    s=input("Enter the name:")     # adding the list of names into an empty string
    if s=="stop":
        print("Completed")
        break
    else:
        name+=s+" "
print(name)
# =========================================================================================================
'''fetch number form user, there will be even and odd numbers, when user inputs 0, print the counts of odd and even and exit'''
even_count=0
odd_count=0
while True:
    num=int(input("Enter the number:"))
    if num==0:
        print(f"Even number = {even_count} and Odd number = {odd_count}")
        break
    elif num%2==0:
        even_count+=1
    else:
        odd_count+=1    
# =========================================================================================================
'''fetch numbers and print the prime numbers among the numbers when 0 is entered'''
prime=''
i=2
while True:
    n=int(input("Enter the number:"))
    count=0
    while i<=n:
        j=1
        while j<=i:
            if i%j==0:
                count+=1
            j+=1
        if count==2:
            prime+=str(i)+' '
        i+=1
    if n==0:
        print(prime)
        break
# =========================================================================================================

'''for loop'''
'''in funtion'''

# =========================================================================================================
list1=[1,2,3,"a","b","c",1.24,"liyana","a"]
for x in list1:
    print(x)
# =========================================================================================================
list1=[1,2,3,"a","b","c",1.24,"liyana","a"]
for x in list1:
    print(x)
else:
    print("Completed")
# =========================================================================================================
'''get a name in a variable and iterate through the variable'''
s=input("Enter the name:")
for i in s:
    print(i)
# =========================================================================================================
'''In a list, add mixed data and put 0 in it, if the current value is 0, then break from the loop and print the previous datas'''
l=[1,"a",4,7,5,90.3,"liya",0,2,4,"hi",9]
for i in l:
    if i==0:
        break
    print(i)
# =========================================================================================================
l=[1,"a",4,7,5,90.3,"liya",0,2,4,"hi",9]
for i in l:
    if i==0:
        continue
    print(i)
# =========================================================================================================

'''for loop'''
'''range funtion'''

# =========================================================================================================
for i in range(2,10,1):   # starting value is included but end value is excluded
    print(i)
# =========================================================================================================
for i in range(2,11,3):
    print(i)
# =========================================================================================================
for i in range(1,10):
    print(i)    # step value by default is 1
# =========================================================================================================
for i in range(10):
    print(i)   # if only 1 value is given, it will be considered as end value and by default start value will be 0
# =========================================================================================================
name="liyana"
for i in range(6):    # length and will print index positions
    print(i)
# =========================================================================================================
name="liyana"
for i in range(len(name)):    # will check length and will print index positions
    print(i)
# =========================================================================================================
name="liyana"
for i in range(len(name)):
    print(i)   
    print(name[i])       # will print the data in the index position
# =========================================================================================================
'''print datas in the odd numbered index position'''
name="liyanafathima"
for i in range(1,len(name),2):
    print(name[i])
# =========================================================================================================
name="liyanafaghadvh"
for i in range(len(name)):
    if i%2!=0:
        print(name[i])
# =========================================================================================================
'''a list containing numbers, print the position of even numbers'''
l=[1,4,6,8,4,8,4,2,3,4,6,7,9]
for i in range(len(l)):
    if l[i]%2==0:
        print(i)
# =========================================================================================================