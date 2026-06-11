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