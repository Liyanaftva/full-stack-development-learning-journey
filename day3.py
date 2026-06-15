#if elif else conditional statement 
mark=int(input("Enter your mark:"))    
if mark>=90:
    print("A Grade")
elif mark>=80:
    print("B Grade")
elif mark>=70:
    print("C Grade")
elif mark>=60:
    print("D Grade")
else:
    print("Failed")
print("All over")
#=================================================
mark=int(input("Enter your mark:"))   #if i give 92 as mark, A grade will be printed, so we need to keep and order, for this comparison operator (and) 
if mark>=80:
    print("A Grade")
elif mark>=90:
    print("B Grade")
elif mark>=70:
    print("C Grade")
elif mark>=60:
    print("D Grade")
else:
    print("Failed")
print("All over")
#=================================================
mark=int(input("Enter your mark:"))    
if 100>=mark>=90:
    print("A Grade")
elif 90>mark>=80:
    print("B Grade")
elif 80>mark>=70:
    print("C Grade")
elif 70>mark>=60:
    print("D Grade")
else:
    print("Failed")
print("All over")
#======================================================
'''a number is odd or even?'''
num=int(input("Enter the number:"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")
#==========================================================
'''a number's last digit is divisible by 4 or not?'''
num=int(input("Enter the number:"))
dig=num%10
if dig%4==0:
    print("The last digit is divisible by 4")
else:
    print("The last digit is not divisible by 4")
#==============================================================
'''fetch a choice from user, i.e, 1,2,3,4,5... and if the user chooses 1, print monday and so on, likeways print all days of the week'''
choice=int(input("Enter your choice of day(1,2,3,4,5,6,7):"))
if choice==1:
    print("It is Monday")
elif choice==2:
    print("It is Tuesday")
elif choice==3:
    print("It is Wednesday")
elif choice==4:
    print("It is Thursday")
elif choice==5:
    print("It is Friday")
elif choice==6:
    print("It is Saturday")
elif choice==7:
    print("It is Sunday")
else:
    print("Invalid Choice")
print("Exit")
#==================================================================
'''fetch a choice from user, i.e, 1,2,3,4,5... and if the user chooses 1, print january and so on, likeways print all months of a year'''
choice=int(input("Enter your choice of month(1,2,3,4,5,6,7,8,9,10,11,12):"))
if choice==1:
    print("It is January")
elif choice==2:
    print("It is February")
elif choice==3:
    print("It is March")
elif choice==4:
    print("It is April")
elif choice==5:
    print("It is May")
elif choice==6:
    print("It is June")
elif choice==7:
    print("It is July")
elif choice==8:
    print("It is August")
elif choice==9:
    print("It is September")
elif choice==10:
    print("It is October")
elif choice==11:
    print("It is November")
elif choice==12:
    print("It is December")
else:
    print("Invalid Choice")
print("Exit")
#=======================================================================
'''nested if'''
choice=int(input("Enter your choice of day(1,2,3,4,5,6,7):"))
if 7>=choice>=1:
    if choice==1:
        print("It is Monday")
    elif choice==2:
        print("It is Tuesday")
    elif choice==3:
        print("It is Wednesday")
    elif choice==4:
        print("It is Thursday")
    elif choice==5:
        print("It is Friday")
    elif choice==6:
        print("It is Saturday")
    else:
        print("It is Sunday")
else:
    print("Invalid Choice")
print("Exit")
#====================================================================
'''giving the users info'''
print("""1:Monday
    2:Tuesday
    3:Wednesday
    4:Thursday
    5:Friday
    6:Saturday
    7:Sunday""")
choice=int(input("Enter your choice of day(1,2,3,4,5,6,7):"))
if 7>=choice>=1:
    if choice==1:
        print("It is Monday")
    elif choice==2:
        print("It is Tuesday")
    elif choice==3:
        print("It is Wednesday")
    elif choice==4:
        print("It is Thursday")
    elif choice==5:
        print("It is Friday")
    elif choice==6:
        print("It is Saturday")
    else:
        print("It is Sunday")
else:
    print("Invalid Choice")
print("Exit")
#================================================================================
'''fetch username from user, we need to set an username already and if they are both equal, print login successful, else print login failed'''
actual_username="user123"
input_username=input("Enter your username:")
if actual_username==input_username:
    print("login successful")
else:
    print("login failed")
#===============================================================================
'''set a username and password and fetch the same from the user and check whether they are both equal'''
actual_username="user123"
actual_password="user@123"
input_username=input("Enter your username:")
input_password=input("Enter your password:")
if actual_username==input_username and actual_password==input_password:
    print("login successful")
else:
    print("login failed")
#=================================================================================  
'''fetch the cost from the user, if the cost is above 100000 then he must give a tax of 15%, if it is btw 50000 and 100000 he must pay a tax of 10%, if it is below 50000 then he must pay a tax of 5%'''
cost=int(input("Enter the cost price:"))
if cost>=100000:
    total_amount=cost*0.15
    print("total tax to be payed is:",total_amount)
elif 100000>cost>=50000:
    total_amount=cost*0.10
    print("total tax to be payed is:",total_amount)
else:
    total_amount=cost*0.05
    print("total tax to be payed is:",total_amount)
#==================================================================================
