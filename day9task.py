'''Keep taking numbers from the user. When the user enters 0, print the total sum and stop.'''
sum=0
while True:
    num=int(input("Enter the number:"))
    sum+=num
    if num==0:
        print(sum)
        break
# =======================================================================================================
'''Keep taking numbers from the user. Stop when a negative number is entered. Print how many positive numbers were entered.'''
positive=0
while True:
    num=int(input("Enter the number:"))
    if num>0:
        positive+=1
    else:
        print("Total number of positive numbers entered are:",positive)
        break
# =======================================================================================================
'''Keep taking numbers from the user until 0 is entered. Print the largest number entered.'''
largest=0
while True:
    num=int(input("Enter the number:"))
    if num==0:
        print("largest =",largest)
        break
    else:
        if num>largest:
            largest=num
# =======================================================================================================
'''Take numbers continuously. When 0 is entered, print the count of even and odd numbers.'''
odd_number=0
even_number=0
while True:
    num=int(input("Enter the number:"))
    if num==0:
        print("odd number =",odd_number,"and even number =", even_number)
        break
    else:
        if num%2==0:
            even_number+=1
        else:
            odd_number+=1
# =======================================================================================================
'''Take a number from the user and print its multiplication table from 1 to 10 using a while loop.'''
n=int(input("Enter the number:"))
i=1
while i<=10:
    mul=n*i
    print(f"{n} x {i} = {mul}")
    i+=1
# =======================================================================================================
'''Take a name from the user and print each character on a new line.'''
name=input("Enter the name:")
for i in name:
    print(i)
# =======================================================================================================
'''Take a string and count how many vowels (a,e,i,o,u) are present.'''
s=input("Enter the string:")
count=0
for i in s:
    if i in {'a','e','i','o','u','A','E','I','O','U'}:
        count+=1
print(count)
# =======================================================================================================
'''Take a string from the user and print it in reverse order.'''
s=input("Enter the string:")
rev=''
l=len(s)
i=l-1
while i>=0:
    rev+=s[i]
    i-=1
print(rev)
# =======================================================================================================
'''Take a string and count uppercase and lowercase letters separately.'''
s=input("Enter the string:")
upper=0
lower=0
for i in s:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print(f"lower case letters = {lower} and upper case letters = {upper}")
# =======================================================================================================
'''Take a string and print characters present at index positions 0, 2, 4, ....'''
s=input("Enter the string:")
for i in range(len(s)):
    if i%2==0:
        print(s[i])
# =======================================================================================================
'''Given a list of numbers, print only the even numbers.'''
l=[1,2,3,4,5,6,7,3,8,4,34,76,3,2,2,21,1,4,5,6,7,5]
for i in l:
    if i%2==0:
        print(i)
# =======================================================================================================
'''Given a list, find and print the largest element.'''
l=[23,44,56,24,5,5,6,7,46,3456,22,345,5567,3234]
largest=0
for i in l:
    if i>largest:
        largest=i
print(largest)
# =======================================================================================================
'''Given a list, count how many times a specific number appears.'''
l=[34,23,2,4,5,6,7,4,6,87,45,3,4,54,5,6,3,3,2,2,56]
count=0
for i in l:
    if i==2:
        count+=1
print(count)
# =======================================================================================================
'''Given a list containing a 0, print all elements before 0.'''
l=[2,3,4,2,4,5,5,0,5,4,3,2,1,5,6,7,8]
for i in l:
    if i==0:
        break
    print(i)
# =======================================================================================================
'''Given a list containing multiple zeros, skip them using continue.'''
l=[2,3,45,0,2,5,6,8,0,3,5,0,3,4,0,7,0,7]
for i in l:
    if i==0:
        continue
    print(i)
# =======================================================================================================