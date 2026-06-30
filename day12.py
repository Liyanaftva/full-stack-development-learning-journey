'''Remove a word from a string'''
s="i love python"
r="python"
new=''
k=''
for i in s:    
        if i!=" ":
            new+=i
        else:
            if new!=" ":
                if new!=r:
                    k+=new
                new=" "
print(k)
# ================================================================================
'''Capitalize the first letter of each word in a sentence'''
s="i love python"
print(s.title())
# ================================================================================

'''PATTERN'''

# ================================================================================
'''Pattern rectange'''
r=3
c=4
for i in range(r):
    for j in range(c):
        print('*',end=' ')
    print()
# ================================================================================
r=4
c=4
for i in range(r):
    for k in range(c):
        print(i,end=" ")
    print()
# ================================================================================
r=3
c=3
for i in range(r):
    for k in range(c):
        print(k+1,end=" ")
    print()
# ================================================================================
'''pattern triangle'''
r=5
c=5
for i in range(r):
    for j in range(c):
        print("*",end=" ")
        if j==i:
            break
    print()
# ================================================================================
r=5
for i in range(r):
    for j in range(i+1):
        print("*",end=" ")
    print()
# ================================================================================
r=5
even=2
for i in range(r):
    for j in range(i+1):
        print(even,end=" ")
        even+=2
    print()
# ================================================================================
'''Pyramid pattern'''
r=5
for i in range(r):
    for j in range(r-i-1):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()
# ================================================================================