name="Liyana"    #string (immutable)
print(name)
print("My name is",name)
print(type(name))
num1=123   #integer (immutable)
print(type(num1))
num2=123.34
print(type(num2))
num3=-234
print(type(num3))
num=123   #type casting
print(type(num))
b=str(num)
print(type(b))
c=float(num)
print(type(c))
a=12   #arithmetic opertors
b=19
c=a+b
print(f"{a}+{b}={c}")
d=a-b
print(f"{a}-{b}={d}")
e=a*b
print(f"{a}x{b}={e}")
f=a/b
print(f"{a}/{b}={f} is the quotient")
g=a//b
print(f"{a}/{b}={g} is the floor value")
h=a%b
print(f"{a}/{b}={h} is the remainder")
i=a**b
print(f"{a}^{b}={i}")
a=45  #comparison operators
b=56
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a>b)
print(a<b)
a=10    #assignment operator
a+=1
print(a)
a-=4
print(a)
a*=5
print(a)
a/=5
print(a)
a%=4
print(a)
a**=2
print(a)
a//=4
print(a)
num1=20  #logical operator
num2=30
num3=num1<num2
print(num3)
num4=num1<num2
print(num4)
print(num3 and num4)
num5=num1>num2
print(num5)
print(num3 and num5)
print(num3 or num5)
print(not num5)
word="python"    #membership operator
print("p" in word)
print("m" in word)
print("n" not in word)
print("l" not in word)
print(str(1) in word)
x=10    #identity operator
y=10
w=34
print(id(x))
print(id(y))
print(x is y) #checks if the memory loc is same or not
print(x is not y)
print(x is w)
print(x is not w)
y+=2
print(id(y))
print(x is y)
a=10
b=a
print(id(a))
print(id(b))
print(a is b)
a+=5
b=a
print(id(a))
print(id(b))
print(a is b)
b+=3
print(id(a))
print(id(b))
print(a is b)
num1=[1,2,3,4,"a"]
num2=[1,2,3,4,"a"]
print(id(num1))
print(id(num2))
num1.append(5)
print(id(num1))
a=[6,5,3,5]
b=[6,5,3,5]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
f=[4,6,8,9]
g=f  #any changes in f affects g as they are equal in terms of assignment operator
print(id(f))
print(id(g))
print(f is not g)
print(f is g)
age=30   #conditional statements (used to make decisions in a program based on the conditions)
if age>=18:
    print("eligible for vote")  #the space is called Indentation
age=14
if age>=18:
    print("eligible for vote")
else:
    print("not eligible for vote")
age=input("Enter your age:")  #input function
print(age)
print(type(age))
age+=2 #error cuz string+integer
age1=int(age) #type casting
age=int(input("Enter your age:"))  #type casting option 2(better)
print(type(age))