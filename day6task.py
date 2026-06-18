'''armstrong number'''
n=int(input('Enter the number:'))
a=n
l=len(str(n))
arm=0
while n>0:
    n1=n%10
    pow=n1**l
    arm+=pow
    n//=10
if arm==a:
    print(f"The number {a} is an armstrong number")
else:
    print(f"The number {a} is not  an armstrong number")
# =============================================================
'''divisor of a number'''
num=int(input("Enter the number:"))
i=1
print(f"The divisors of {num} are:")
while i<=num:
    if num%i==0:
        print(i)
    i+=1
# ============================================================== 
'''reverse of a string'''
s=input("Enter the string:")
rev=''
l=len(s)
ind=l-1
while ind>=0:
    rev+=s[ind]
    ind-=1
print(f"The reverse of the string {s} is",rev)
# ===============================================================
'''prime number'''
num=int(input("Enter the number:"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i+=1
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
# ===============================================================
'''digit sum'''
num=int(input("Enter the number:"))
sum=0
a=num
while num>0:
    last=num%10
    sum+=last
    num//=10
print(f"The digit sum of the number {a} is",sum)
# ==============================================================
'''reverse of a number'''
num=int(input("Enter the number:"))
a=num
rev=''
while num>0:
    last=num%10
    rev+=str(last)
    num//=10
print(f"The reverse of the number {a} is",rev)
# ==============================================================
'''palindrome or notpalindrome'''
num=int(input("Enter the number:"))
a=num
rev=''
while num>0:
    last=num%10
    rev+=str(last)
    num//=10
if a==int(rev):
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
# ===============================================================