i=1  #while loop
while i<=5:
    print(i)    #infinite loop since the value of i is always 1.
# ================================================================
i=1
while i<=5:
    print(i)
    i+=1
# ================================================================
i=1
while i<=5:
    print(i)
    i+=1
else:                #else part works when condition becomes false
    print("Completed")
# ================================================================
m=1
while m<=10:    #variable initialized may not be the one we would want ot print, but it occurs as the number of times loop is to be executed
    print("Hello world!!!")
    m+=1
else:
    print("Completed")
# ==================================================================
i=10
while i>=1:
    print(i)
    i-=1
else:
    print("Completed")
# ===================================================================
i=2      #1st method
while i<=50:
    print(i)
    i+=2
else:
    print("Completed")
# ===================================================================
i=1    #2nd method
while i<=50:
    if i%2==0:
        print(i)
    i+=1
else:
    print("Completed")
# ===================================================================
'''sum of 1st n numbers'''
i=1
sum=0
num=10
while i<=num:
    sum+=i
    i+=1
print(f"sum of 1st {num} numbers is =",sum)
# =================================================================
'''fetch input from user and find the sum of n numbers'''
start=int(input("Enter the starting number:"))
a=start
end=int(input("Enter the ending number:"))
sum=0
while start<=end:
    sum+=start
    start+=1
print(f"sum of {a} to {end} numbers is =",sum)
# ====================================================================
'''factorial of a number'''
i=1
num=int(input("Enter the number to find the factorial:"))
fact=1
while i<=num:
    fact*=i
    i+=1
print(f"The factorial of {num} is = ",fact)
# ====================================================================
name="liyana"
print(name[0])   #index
print(name[1])
print(name[5])
# =======================================================================
a=str(input("Enter a word:"))
ind=len(a)-1
rev=''   #empty string
while ind>=0:
    rev+=a[ind]
    ind-=1
print(f"Reverse of the string {a} is =",rev)
# ======================================================================