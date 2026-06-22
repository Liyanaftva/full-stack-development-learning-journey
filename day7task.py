'''Print multiplication tabel of a given number (format : 1x1=1)'''
num1=int(input("Enter the number to find the multiplication table:"))
num2=int(input("Enter the number till which the multiplication table is to be found:"))
i=1
mul=1
while  i<=num2:
    mul=num1*i
    print(f"{num1} x {i} =",mul)
    i+=1
# ==================================================================================================
'''Print the fibonacci series'''
num1=int(input("Enter the number of terms:"))
n1=0
n2=1
i=1
print(n1,n2,end=' ')
while i<=num1:
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=' ')
    i+=1
# ==================================================================================================
'''Counting digits in a number (eg: 123 = 3)'''
num1=int(input("Enter the number:"))
i=1
count=0
while i<=len(str(num1)):
    count+=1
    i+=1
print(count)
# ==================================================================================================
'''Count the even digits in number'''
num1=int(input("Enter the number:"))
a=num1
i=1
count=0
while i<=len(str(a)):
    mod=num1%10
    num1//=10
    if mod%2==0:
        count+=1
    i+=1
print(count)
# ==================================================================================================
'''Check whether a number is perfect (the sum of divisors of a number is equal to the number)'''
num1=int(input("Enter the number:"))
a=num1
i=1
sum=0
while i<num1:
    if num1%i==0:
        sum+=i
    i+=1
if sum==a:
    print(f"The number {num1} is perfect")
else:
    print(f"The number {num1} is not perfect")
# ==================================================================================================
# '''Product of the digits of a number'''
num1=int(input("Enter the number:"))
a=num1
i=1
mul=1
while i<=len(str(a)):
    mod=num1%10
    num1//=10
    mul*=mod
    i+=1
print(f"Products of the digits of the number {a} is",mul)
# ==================================================================================================
'''Print prime numbers upto n (fetch the ending number from the user)'''
num1=int(input("Enter the number upto which you need the prime number:"))
i=2
print(f"The prime numbers upto {num1} are:",end=' ')
while i<=num1:
    count=0
    j=1
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,end=' ')
    i+=1 
# ==================================================================================================
'''Print all the numbers divisible by 5 from 1 to n'''
n=int(input("Enter the number till which you need to find the numbers divisible by 5:"))
i=1
print(f"The numbers divisible by 5 till {n} are:", end=' ')
while i<=n:
    if i%5==0:
       print(i,end=' ')
    i+=1
# ==================================================================================================
'''Find the largest digit of a number'''
num1=int(input("Enter the number:"))
a=num1
large=0
i=1
while i<=len(str(a)):
    digit=num1%10
    if digit>large:
        large=digit
    num1//=10
    i+=1
print(large)
# ==================================================================================================