# =========================================================================================================

"""SELF PRACTICE QUESTIONS (NOT TAUGHT AT ACADEMY)"""

# =========================================================================================================

'''Q1. Compress Consecutive Characters
Given a string, replace every consecutive group by the character followed by its count.
Input:
bbbccaaaaadd
Output:
b3c2a5d2'''
s = 'bbbccaaaaadd'
count = 1
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    else:
        print(s[i], count, end='', sep='')
        count = 1
print(s[-1], count, end='', sep='')
# =========================================================================================================

'''Q2. Count Valid Substrings
Count all non-empty substrings that start and end with the same character.
Input:
ababa
Output:
9'''
s = 'ababa'
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i] == s[j]:
            count += 1
print(count)
# =========================================================================================================

'''Q3. Missing Number
Numbers from 1 to N are given with exactly one number missing.
Find the missing number.
Input:
1 2 3 4 6 7 8
Output:
5'''
numbers = [1, 2, 3, 4, 6, 7, 8]
for i in [1, 2, 3, 4, 5, 6, 7, 8]:
    if i not in numbers:
        print(i)
# =========================================================================================================

'''Q4. Remove Consecutive Duplicates
Remove consecutive duplicate characters.
Input:
aaabbbbccaadd
Output:
abcad'''
s = 'aaabbbbccaadd'
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        print(s[i], end='', sep='')
print(s[-1])
# =========================================================================================================

'''Q5. First Non-Repeating Character
Find the first character that appears only once.
Input:
statistics
Output:
a'''
s = 'statistics'
store = ''
for i in s:
    count = 0
    if i not in store:
        for j in s:
            if j == i:
                count += 1
        if count == 1:
            print(i)
            break
        store += i
# =========================================================================================================

'''Q6. Find Duplicate Number
Exactly one number appears twice.
Input:
1 4 5 2 3 6 5
Output:
5'''
s = [1, 4, 5, 2, 3, 6, 5]
store = []
for i in s:
    count = 0
    if i not in store:
        for j in s:
            if j == i:
                count += 1
        if count >= 2:
            print(i)
            break
        store.append(i)
# =========================================================================================================

'''Q7. Character Frequency
Print every character with its frequency.
Input:
programming
Output:
p 1
r 2
o 1
g 2
a 1
m 2
i 1
n 1'''
s = 'programming'
store = ''
for i in s:
    count = 0
    if i not in store:
        for j in s:
            if j == i:
                count += 1
        print(i, count)
    store += i
# =========================================================================================================

'''Q8. Rotate Array Left by One
Rotate the array one position to the left.
Input:
10 20 30 40 50
Output:
20 30 40 50 10'''
array = [10, 20, 30, 40, 50]
rev_array = []
for i in range(len(array) - 1):
    rev_array.append(array[i + 1])
rev_array.append(array[0])
print(rev_array)
# =========================================================================================================

'''Q9. Find the Largest Number
Find the largest number in the array.
Input:
12 45 2 89 34 67
Output:
89'''
l = [12, 45, 2, 89, 34, 67]
largest = l[0]
for i in l:
    if i >= largest:
        largest = i
print(largest)
# =========================================================================================================

'''Q10. Count Digits
Count how many digits are present in the given string.
Input:
abc123xy45
Output:
5'''
s = 'abc123xy45'
count = 0
for i in s:
    if i in '0123456789':
        count += 1
print(count)
# =========================================================================================================

'''Q11. Move All Zeros to the End
Move all zeros to the end while maintaining the order of the other elements.
Input:
1 0 3 0 5 2 0
Output:
1 3 5 2 0 0 0'''
l = [1, 0, 3, 0, 5, 2, 0]
nz = []
z = []
for i in l:
    if i != 0:
        nz.append(i)
    else:
        z.append(i)
nz.extend(z)
print(nz)
# =========================================================================================================

'''Q12. Count Uppercase and Lowercase Letters
Count the number of uppercase and lowercase letters.
Input:
PyThOn
Output:
Uppercase = 3
Lowercase = 3'''
s = "PyThOn"
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("Uppercase =", upper)
print("Lowercase =", lower)
# =========================================================================================================