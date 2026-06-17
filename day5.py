'''nested if conditional statement'''
num=int(input("Enter a number:"))
if num>0:
    if num%2==0:
        print(f"Number {num} is positive and even")
    else:
        print(f"Number {num} is positive and odd")
elif num==0:
    print(f"Number {num} is zero")
else:
    print(f"Number {num} is negative")
#=======================================================================================
'''if number is positive, then check whether it is even, if it is even, check whether it is greater than 10'''
num=int(input("Enter a number:"))
if num>0:
    if num%2==0:
        if num>10:
            print(f"Number {num} is positive and even and is greater than 10")
        elif num==10:
            print(f"Number {num} is positive and even and is equal to 10")
        else:
            print(f"Number {num} is positive and even and is less than 10")
    else:
        print(f"Number {num} is positive and odd")
elif num==0:
    print(f"Number {num} is zero")
else:
    print(f"Number {num} is negative")
#============================================================================================
'''voting eligitbility:
    # age
    # age is above 18
    # valid id'''
age=int(input("Enter your age:"))
if age>=18:
    id=input("Do you have a valid id proof {YES/NO}:")
    if id=="YES" or id=="yes" or id=="Yes" or id=="y" or id=="Y":
        print("You are eligible for vote")
    else:
        print("You are eligible for vote by age, but you need to submit any valid ID")
else:
    print("You are not eligible to vote")
#=============================================================================================
'''check if a number is 3 digit, if it is, then check whether it is even or not'''
num=int(input("Enter the number:"))
if len(str(num))==3:
    if num%2==0:
        print(f"The number {num} is a 3-digit number and is an even number")
    else:
        print(f"The number {num} is a 3-digit number and is an  odd number")
else:
    print(f"The number {num} is not a 3-digti number")
#============================================================================================
'''check if a number is 4-digit and if it ends with zero'''
num=int(input("Enter the number:"))
if len(str(num))==4:
    if num%10==0:
        print(f"The number {num} is a 4-digit number and it ends with zero")
    else:
        print(f"The number {num} is a 4-digit number and it does not ends with zero")
else:
    print(f"The number {num} is not a 4-digit number")
#============================================================================================
'''get username, password, if both are correct, login successful'''
actual_username="user123"
actual_password="user@123"
get_username=input("Enter the username:")
if actual_username==get_username:
    get_password=input("Enter the password:")
    if actual_password==get_password:
        print("Login Successfull")
    else:
        print("Login Failed. Incorrect Password. TRY AGAIN!!!")
else:
    print("Login Failed. Incorrect Username. TRY AGAIN!!!")
# #=============================================================================================
'''a number is divisible by 3,5 and 8'''
num=int(input("Enter the number:"))
if num%3==0:
    if num%5==0:
        if num%8==0:
            print(f"The number {num} is divisble by 3, 5 and 8")
        else:
            print(f"The number {num} is only divisible by 3 and 5, it is not divisible by 8")
    elif num%8==0:
        if num%5==0:
            print(f"The number {num} is divisble by 3, 8 and 5")
        else:
            print(f"The number {num} is only divisible by 3 and 8, it is not divisible by 5")    
    else:
        print(f"The number {num} is only divisible by 3, it is not divisible by 5 and 8")
elif num%5==0:
    if num%8==0:
        print(f"The number {num} is divisble by 5 and 8, it is not divisible by 3 ")
    else:
        print(f"The number {num} is only divisible by 5, it is not divisible by 8 and 3")
elif num%8==0:
    print(f"The number {num} is only divisible by 8, it is not divisible by 3 and 5")
else:
    print(f"The number {num} is not divisible by 3, 5 and 8")
#================================================================================================