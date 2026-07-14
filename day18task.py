# =========================================================================================================

"""SELF PRACTICE QUESTIONS - SET 2"""

# =========================================================================================================

'''Q1. Reverse Words Order
Reverse the order of the words in a sentence.
Input:
I love python
Output:
python love I'''

s = 'I love python'
words = s.split()
rev = ''
print(words)
for i in range(len(words)-1, -1, -1):
    rev += words[i] + ' '
print(rev)
# =========================================================================================================

'''Q2. Second Largest Distinct Number
Find the second largest DISTINCT number in the array.
Input:
8 3 15 7 15 9 8
Output:
9'''

array = [8, 3, 15, 7, 9, 8]
store = []
for i in array:
    if i not in store:
        store.append(i)
print(store)
large = store[0]
sec_large = store[0]
for i in store:
    if i > large:
        sec_large = large
        large = i
    elif i > sec_large and i != large:
        sec_large = i
print(sec_large)
# =========================================================================================================

'''Q3. Second Smallest Distinct
Find the second smallest DISTINCT number.
Input:
8 3 15 7 15 9 8
Output:
7'''
array = [8, 3, 15, 7, 15, 9, 8]
store = []
for i in array:
    if i not in store:
        store.append(i)
small = store[0]
second = store[0]
for i in store:
    if i < small:
        second = small
        small = i
    elif i < second and i != small:
        second = i
print(second)
# =========================================================================================================