# """SELF PRACTICE QUESTIONS, NOT TAUGHT AT ACADEMY"""
 
'''Question 1: String Compression
Problem Statement: Given a string, compress consecutive occurrences of the same character by
replacing them with the character followed by its count.
Sample Input
aaabbcaaa
Sample Output
a3b2c1a3'''

s="aaabbcaaa"
i=0
l=len(s)
while i<l:
    current=s[i]
    count=1
    while i<l-1 and current==s[i+1]:
        count+=1
        i+=1
    print(current,count,sep='',end='')
    i+=1
# ======================================================================================================
'''Question 2: Remove Consecutive Duplicates
Problem Statement: Given a string, remove consecutive duplicate characters and keep only one
occurrence from each group.
Sample Input
aaabbccdaa
Sample Output
abcda'''

s="aaabbccdaa"
i=0
l=len(s)
while i<l:
    current=s[i]
    count=1
    while i<l-1 and current==s[i+1]:
        count+=1
        i+=1
    if count>=1:
        print(current,sep='',end='')
    i+=1
# ======================================================================================================
'''Question 3: Character Frequency Count
Problem Statement: Given a string, print the frequency of each character.
Sample Input
banana
Sample Output
b:1 a:3 n:2'''

s="banana"
i=0
l=len(s)
printed=''
while i<l:
    current=s[i]
    if current not in printed:
        count=0
        j=0
        while j<l:
            if s[j]==current:
                count+=1
            j+=1
        print(f"{current}:{count}", end=' ')
        printed+=current
    i+=1
# ======================================================================================================
'''Question 4: First Non-Repeating Character
Problem Statement: Find the first character that appears exactly once.
Sample Input
aabbcdeff
Sample Output
c'''

s="aabbcdeff"
i=0
l=len(s)
while i<l:
    current=s[i]
    count=0
    j=0
    while j<l:
        if s[j]==current:
            count+=1
        j+=1
    if count==1:
        print(current)
        break
    i+=1
# ======================================================================================================
'''Question 5: First Repeating Character
Problem Statement: Find the first character that repeats.
Sample Input
abcaef
Sample Output
a'''

s="abcaef"
i=0
l=len(s)
while i<l:
    current=s[i]
    count=0
    j=0
    while j<l:
        if current==s[j]:
            count+=1
        j+=1
    if count>=2:
        print(current)
        break
    i+=1
# ======================================================================================================
'''Question 6: Reverse a String
Problem Statement: Reverse the given string.
Sample Input
hello
Sample Output
olleh'''

s="hello"
l=len(s)
i=l-1
rev=''
while i>=0:
    rev+=s[i]
    i-=1
print(rev)
    
# ======================================================================================================