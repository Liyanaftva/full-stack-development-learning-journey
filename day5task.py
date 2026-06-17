'''Find the greater number between two numbers using nested if.'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>=num2:
    if num1>num2:
        print(f"The number {num1} is greater than {num2}")
    else:
        print(f"The numbers {num1} and {num2} are both equal")
else:
    print(f"The number {num2} is greater than {num1}")
#==================================================================
'''Check whether a student has passed.
       # Marks ≥ 40
       # Attendance ≥ 75%'''
mark=int(input("Enter the student's mark:"))
if mark>=40:
    attendance=float(input("Enter the attendance percentage of student (format:10, 20, 45.6):"))
    if attendance>=75:
        print("The student has passed the exams")
    else:
        print("The student did not pass the exams due to attendance shortage")
else:
    print("The student has failed")
#===================================================================
'''Find the largest among three numbers using nested if.'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>=num2:
    if num1>=num3:
        print(f"{num1} is greater than {num2} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num2}")
elif num2>=num1:
    if num2>=num3:
        print(f"{num2} is greater than {num1} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num2}")
else:
    print("invalid")
#===================================================================
'''Determine the grade of a student:
     # Marks ≥ 90 → A
     # Marks ≥ 75 → B
     # Marks ≥ 60 → C
     # Otherwise → Fail'''
mark=int(input("Enter the mark of the student:"))
if 0<=mark<=100:
    if mark>=60:
        if mark>=75:
            if mark>=90:
                print("A Grade")
            else:
                print("B Grade")
        else:
            print("C Grade")
    else:
        print("Failed")
else:
    print("Invalid mark")
#=====================================================================
'''ATM Withdrawal Program
     # PIN must be correct.
     # Balance must be sufficient.
     # Amount must be a multiple of 100.'''
pin=2347
balance=30000
get_pin=int(input("Enter the PIN:"))
if pin==get_pin:
    choice=input("Do you want to withdraw the money?(YES/NO)")
    if choice=="YES" or choice=="yes" or choice=="y" or choice=="Y" or choice=="Yes":
        money=int(input("Enter the amount to be withdrawed:"))
        if money<=balance:
            if money%100==0:
                print("Withdrawed money=",money)
                print("Total balance=",balance-money)
            else:
                print("Money to be withdrawed must be a multiple of 100")
        else:
            print("Balance insufficient")
    else:
        print("User inputted money not to be withdrawed")
else:
    print("Incorrect PIN, try again!!!")
#======================================================================  
'''Login System
    # Username must be correct.
    # Password must be correct.
    # OTP must be correct.'''
actual_username="user123"
actual_password="user@123"
actual_OTP=2345
get_username=input("Enter your username:")
if actual_username==get_username:
    get_password=input("Enter the password:")
    if actual_password==get_password:
        get_OTP=int(input("Enter the OTP:"))
        if actual_OTP==get_OTP:
            print("Login Successfful")
        else:
            print("Login failed, due to incorrect OTP!!")
    else:
        print("Login failed, due to incorrect password!!")
else:
    print("Login failed, due to incorrect username!!")
#======================================================================    
'''Admission Eligibility
     #Age ≥ 17
     # Marks ≥ 60
     # Entrance Exam ≥ 50'''
age=int(input("Enter the age:"))
if age>=17:
    mark=int(input("Enter the mark:"))
    if mark>=60:
        entrance=int(input("Enter the entrance score:"))
        if entrance>=50:
            print("Eligible for admission")
        else:
            print("Not eligible for admission, because of low entrance score")
    else:
        print("Not eligible for admission, because of low mark")
else:
    print("Not eligible for admission")
#======================================================================
'''Employee Bonus Calculation
      # Experience > 5 years
      # Salary < 50000
      # Then give 10% bonus '''
experience=int(input("Enter your years of experience:"))
if experience>5:
    salary=float(input("Enter your current salary:"))
    if salary<50000:
        bonus=salary*0.10
        print("Bonus incremented =",bonus)
        total=salary+bonus
        print("Total salary =", total)
    else:
        print("Salary too high!!")
else:
    print("Experience not sufficient")
#======================================================================
'''Determine whether a number is:
      # Positive
      # Even
      # Divisible by 5'''
num=int(input("Enter the number:"))
if num%5==0:
    if num%2==0:
        if num>0:
           print(f"{num} is divisible by 5 and is even and is positive") 
        else:
            print(f"{num} is divisible by 5 and is even and is negative") 
    else:
        print(f"{num} is divisible by 5 and is odd")
else:
    print(f"{num} is not divisble by 5")
# ======================================================================
'''Bank Loan Eligibility
      # Age ≥ 21
      # Salary ≥ 25000
      # Credit Score ≥ 700'''
age=int(input("Enter the age:"))  
if age>=21:
    salary=float(input("Enter the salary:"))
    if salary>=25000:
        credit=int(input("Enter the credit score:"))
        if credit>=700:
            print("Eligible for bank loan")
        else:
            print("Not eligible for bank loan due to low credit score")
    else:
        print("Not eligible for bank loan due to low salary")
else:
    print("Not eligible for bank loan") 
# ======================================================================
'''Blood Donation Eligibility
      # Age between 18 and 60
      # Weight ≥ 50 kg'''
age=int(input("Enter the age:"))  
if 18<=age<=60:
    weight=float(input("Enter the weight:"))
    if weight>=50:
        print("Eligible for blood donation")
    else:
        print("Not eligible for blood donation due to insufficient weight")
else:
    print("Not eligible for blood donation")
# ======================================================================