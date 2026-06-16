'''Write a Python program to check whether a given number is divisible by 2, 3, 4, and 6.'''
num=int(input("Enter the number:"))
if num%2==0 and num%3==0 and num%4==0 and num%6==0:
    print(f"The number {num} is divisible by all the integers 2, 3, 4, and 6.")
else:
    print(f"The number {num} is not divisble by all the integers 2, 3, 4, and 6.")
#======================================================================================================
'''Write a Python program to calculate the electricity bill based on the following conditions:
#   For the first 100 units, no charge is applied.
#   For units between 101 and 300, charge ₹5 per unit for every unit above 100.
#   For units above 300, charge:
#   ₹5 per unit for the next 200 units (101–300)
#   ₹10 per unit for every unit above 300. Display the total bill amount.'''
unit=int(input("Enter the number of units:"))
if unit<=100:
    print("No charges applied")
elif 101<=unit<=300:
    charge=(unit-100)*5
    print("Total Charges applied is",charge)
else:
    part1=100
    part2=unit-300
    part3=unit-part1-part2
    charge1=part3*5
    charge2=part2*10
    total=charge1+charge2
    print("Total Charges applied is",total)
#=======================================================================================================
'''Write a program to check whether a character is a vowel.'''
char=input("Enter the character to check whether it is vowel or not:")
if char in ['A','E','I','O','U','a','e','i','o','u']:
    print("Character is vowel")
else:
    print("Character is not vowel")
#=======================================================================================================
'''Write a program to check whether a number is greater than 100.'''
num=int(input("Enter the number:"))
if num>100:
    print("The number is greater than 100")
elif num==100:
    print("The number is equal to 100")
else:
    print("The number is less than 100")
#=======================================================================================================
'''Write a program to check whether a year is a leap year.'''
year=int(input("Enter the year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
#=======================================================================================================
'''Write a program to check whether a number is a multiple of 10.'''
num=int(input("Enter the number:"))
if num%10==0:
    print("It is a multiple of 10.")
else:
    print("It is not a multiple of 10")
#=======================================================================================================
'''Write a program to display "Adult" if age is 18 or above.'''
age=int(input("Enter the age:"))
if age>=18:
    print("Adult")
else:
    print("Not an Adult")
#=======================================================================================================
'''Write a program to check whether a password length is greater than 8.'''
password=input("Enter the password:")
if len(password)>8:
    print("Length of the password is greater than 8 and is accepted")
else:
    print("Length of the password is less than 8 and is declined")
#=======================================================================================================
'''Write a program to compare two ages and display the older person.'''
age1=int(input("Enter the age of the first person:"))
age2=int(input("Enter the age of the second person:"))
if age1>age2:
    print("The first person is older")
elif age1<age2:
    print("The second person is older")
else:
    print("The first and second person have same age")
#=======================================================================================================
'''Write a program to check whether a number is a multiple of both 3 and 5.'''
num=int(input("Enter the number:"))
if num%3==0 and num%5==0:
    print(f"The number {num} is divisible by both 3 and 5")
else:
    print(f"The number {num} is not divisible by both 3 and 5")
#=======================================================================================================
'''Write a program to find the largest of three numbers.'''
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print(f"{a} is the largest of {a},{b}, and {c}")
elif b>=a and b>=c:
    print(f"{b} is the largest of {a},{b}, and {c}")
else:
    print(f"{c} is the largest of {a},{b}, and {c}")
#=======================================================================================================
'''Write a program to create a simple calculator (+, -, *, /).'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
opr=input("Enter the operation to perform (+, -, *, /):")
if opr=="+":
    result=num1+num2
    print (result)
elif opr=="-":
    result=num1-num2
    print (result)
elif opr=="*":
    result=num1*num2
    print (result)
else:
    if num2==0:
        print("Division not possibe.")
    else:
        result=num1/num2
        print (result) 
#=======================================================================================================
'''Write a program to determine whether a number is positive, negative, or zero.'''
num=int(input("Enter the number:"))
if num>0:
    print(f"{num} is positive number")
elif num==0:
    print(f"{num} is zero")
else:
    print(f"{num} is negative number")
#=======================================================================================================
'''Write a program to Check whether a number is a 2-digit, 3-digit, or 4-digit number.'''
num=int(input("Enter the number:"))
if 10<=num<100:
    print(f"{num} is 2-digit number")
elif 100<=num<1000:
    print(f"{num} is 3-digit number")
elif 1000<=num<10000:
    print(f"{num} is 4-digit number")
else:
    print(f"{num} is either 1-digit or greater than 4-digit number")
#=======================================================================================================
'''Create an ATM menu using if-elif-else.'''
print('''1. Cash Deposit\n2. Cash Withdrawal\n3. Check Balance''')
choice=int(input("Enter the choice(1,2,3):"))
balance=200000
if choice==1:
    print("Deposit the Cash")
    deposit=int(input("Enter the amount to be deposited:"))
    print("Deposited money=",deposit)
    print("Total updated bank balance=",balance+deposit)
elif choice==2:
    print("Withdraw the Cash")
    withdraw=int(input("Enter the amount to be withdrawed:"))
    print("Withrawed money=",withdraw)
    print("Total updated bank balance=",balance-withdraw)
elif choice==3:
    print("Check the bank balance")
    print("Total bank balance=",balance)
else:
    print("Invalid choice, Try again")
#=======================================================================================================
'''Enter battery percentage.
        #          Above 80 → "Battery Full"
        #          30 to 80 → "Battery Normal"
        #          Below 30 → "Charge Immediately" '''
battery=int(input("Enter your battery percentange:"))
if battery>80:
    print("Battery is full")
elif 30<=battery<=80:
    print("Battery is normal")
else:
    print("Charge immediately")
#=======================================================================================================
'''Salary Increment
       # Salary < 20000 → 20% Increment
       # Salary < 50000 → 10% Increment
       # Salary ≥ 50000 → 5% Increment  '''
salary=int(input("Enter your salary:"))
if salary<20000:
    increment=salary*0.20
elif salary<50000:
    increment=salary*0.10
else:
    increment=salary*0.05
total=salary+increment
print("increment is:",increment)
print("total salary is:",total)
#========================================================================================================
'''Age Group Classifier
            # 0–12 → Child
            # 13–19 → Teenager
            # 20–59 → Adult
            # 60+ → Senior Citizen'''
age=int(input("Enter the age:"))
if 0<=age<=12:
    print("The person is a Child")
elif 13<=age<=19:
    print("The person is a Teenager")
elif 20<=age<=59:
    print("The person is an Adult")
else:
    print("The person is a Senior Citizen")
#=========================================================================================================
'''Restaurant Rating
    # Based on rating:

         # 5 → Excellent
         # 4 → Very Good
         # 3 → Good
         # 2 → Average
         # 1 → Poor '''
print('''5 → Excellent
         4 → Very Good
         3 → Good
         2 → Average
         1 → Poor ''')
rate=int(input("Enter the rating(1,2,3,4,5):"))
if rate==5:
    print("Excellent")
elif rate==4:
    print("Very Good")
elif rate==3:
    print("Good")
elif rate==2:
    print("Average")
elif rate==1:
    print("Poor")
else:
    print("Invalid input")
#==========================================================================================================