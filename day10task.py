'''Print numbers from a list. If 5 is found, stop the loop.'''
l=[1,3,3,2,1,4,6,7,57,77,5,3,5,6,67,8]
for i in l:
    if i==5:
        break
    print(i)
# ============================================================================================
'''Print numbers from 1 to 20 but skip multiples of 3.'''
for i in range(1,21):
    if i%3==0:
        continue
    print(i)
# ============================================================================================
'''Keep taking strings from the user. Stop when the user enters "exit".'''
while True:
    s=input("Enter the string:")
    if s=="exit" or s=="Exit" or s=="EXIT":
        break
# ============================================================================================
'''Take 10 numbers from the user and print only positive numbers.'''
count=1
s=''
while True:
    num=int(input("Enter the number:"))
    count+=1
    if num>0:
        s+=str(num)+" "
    if count>10:
        break
print(s)
# ============================================================================================
'''Keep taking numbers until 0 is entered and print:
Sum
Average
Even count
Odd count
Largest number'''
sum=0
even=0
odd=0
large=0
count=0
while True:
    num=int(input("Enter the number:"))
    if num==0:
        print(f"sum = {sum}, average = {avg}, even count = {even}, odd count = {odd}, largest = {large}")
        break
    else:
        count+=1
        sum+=num
        if num%2==0:
            even+=1
        else:
            odd+=1
        if num>large:
            large=num
    avg=sum/count
# ============================================================================================
'''Take a string and count how many digits are present.'''
s="dgfvk3634786439hdhjkd"
count=0
for i in s:
    if i in '0123456789':
        count+=1
print(count)
# ============================================================================================
'''Take a sentence and count the number of spaces.'''
s=" i  love  python"
count=0
for i in s:
    if i==" ":
        count+=1
print(count)
# ============================================================================================
'''Take a sentence and print it without spaces.'''
s='i love python'
sen=''
for i in s:
    if i!=" ":
        sen+=i
print(sen)
# ============================================================================================