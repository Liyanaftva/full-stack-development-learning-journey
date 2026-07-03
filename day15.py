# ======================================================================================

'''SEQUENCE DATA TYPES'''

# ======================================================================================
'''LIST COMPREHENSION'''
# SHORT AND POWERFUL WAY TO CREATE LIST IN PYTHON USING A SINGLE LINE OF CODE
# it consist of an expression by a for clause. and optionally. one or more if clauses
# syntax : variable = [expression for item in iterable if condition]
# expression is evaluated for each item in iterable, and if condition is true the result is included in the new list
# order: for loop->if condition->expression->stores in variable
# while loops are not used in the list comprehension
# ======================================================================================
'''Create a list of squares of numbers of a given list'''
list1=[1,2,3,4]
list2=[]
for i in list1:
    list2.append(i*i)
print(list2)
# ======================================================================================
'''Create a list of squares of numbers of a given list using list comprehension'''
list1=[1,2,3,4]
list2=[k*k for k in list1]
print(list2)
# ======================================================================================
'''Create a list of squares of even numbers of a given list'''
l1=[1,2,3,4,5,6,7,8,9]
l2=[k*k for k in l1 if k%2==0]
print(l2)
# ======================================================================================
'''Create a list of even numbers from 0 to 50'''
l=[k for k in range(51) if k%2==0]
print(l)
# ======================================================================================
'''convert the letters of string to uppercase and store it in a list'''
s="liyana"
l=[k.upper() for k in s]
print(l)
# ======================================================================================
'''create a list of tuples containing numbers and their squares'''
l=[1,2,3,4,5,6,7,8,9]
l1=[(k,k*k) for k in l]
print(l1)
# ======================================================================================
'''capitalize the first letter of each word of a sentence'''
s="i love python"
l2=s.split()
l1=[k.capitalize() for k in l2]
print(l1)
# ======================================================================================
'''word contaning letter a'''
l=['liyana','arun','zihr','kiren','olive','max','jiger']
l2=[k for k in l if 'a' in k]
print(l2)
# ======================================================================================
'''create a list containing words starting with the letter b'''
l=['joke','ball','hari','balloon','baron','bull','lion','big']
l1=[k for k in l if k[0]=='b']
print(l1)
# ======================================================================================
'''print 1 if present else print 0 in other numbers place'''
l=[1,2,3,1,5,1,'s',1,3,0,6,4,1]
l1=[k if k==1 else 0 for k in l]
print(l1)
# ======================================================================================
'''print numbers containing 6 from 1 to 100'''
l=[k for k in range(101) if '6' in str(k)]
print(l)
# ======================================================================================
'''create a list containing capital letter of each word in a list'''
l=['anu','minu','ponnu','chinnu']
l1=[k.capitalize() for k in l]
l2=[k[0] for k in l1]
print(l2)
# ======================================================================================
'''print vowels from a sentence to a new list'''
s="i love python"
l=[k for k in s if k in 'aeiouAEIOU']
print(l)
# ======================================================================================
'''Store words whose first and last letters are the same and count them'''
l=['aba','farah','nanaa','lol','girirsh','nunan']
l2=[k for k in l if k[0]==k[-1]]
print(l2)
print("count = ",len(l2))
# ======================================================================================
'''Create a list of cubes of numbers from 1 to 10.'''
l=[k**3 for k in range(1,11)]
print(l)
# ======================================================================================
'''Create a list containing only odd numbers from 1 to 50.'''
l=[k for k in range(51) if k%2!=0]
print(l)
# ======================================================================================
'''Create a list of the lengths of each word.'''
l=['aba','farah','nanaa','lol','girirsh','nunan']
l1=[len(k) for k in l]
print(l1)
# ======================================================================================
'''Convert every word in a list to lowercase.'''
l=["Arun","gOuRi","AnU","LithEsH","KorA"]
l1=[k.lower() for k in l]
print(l1)
# ======================================================================================
'''Store only numbers greater than 50.'''
l=[1,23,46,78,33,56,78,3,67,43,23,46,78]
l1=[k for k in l if k>50]
print(l1)
# ======================================================================================
'''Store only words whose length is greater than 5.'''
l1=['arun','giresh','hour','leeyan','kiren','liyana','loyan']
l=[k for k in l1 if len(k)>5]
print(l)
# ======================================================================================
'''Create a list of the first letter of every word.'''
s="i love python"
l1=s.split()
l=[k[0] for k in l1]
print(l)
# ======================================================================================
'''Create a list of the last letter of every word.'''
s="i love python so much"
l1=s.split()
l=[k[-1] for k in l1]
print(l)
# ======================================================================================
'''Store only palindrome words.'''
l=['madam','mango','lol','kangaroo','irony','king','malayalam','orange','nana','bob']
l1=[k for k in l if k==k[::-1]]
print(l1)
# ======================================================================================
'''Store only words containing the letter e.'''
l=['maya','arun','leon','arya','kiera','leyara','noel','arunima']
l1=[k for k in l if 'e' in k]
print(l1)
# ======================================================================================
'''Store words that start with a vowel.'''
l=['maya','arun','leon','arya','kiera','leyara','noel','arunima','ira','ouran','urani','elara']
l1=[k for k in l if k[0] in 'aeiouAEIOU']
print(l1)
# ======================================================================================
'''Store words that end with a vowel.'''
l=['maya','arun','leon','arya','kiera','leyara','noelle','arunima','ira','ouran','urani','elara']
l1=[k for k in l if k[-1] in "aeiouAEIOU"]
print(l1)
# ======================================================================================
'''Store numbers divisible by both 3 and 5 from 1-100.'''
l1=[k for k in range(101) if k%3==0 and k%5==0]
print(l1)
# ======================================================================================
'''Store the square of odd numbers only.'''
l=[1,23,15,46,78,33,56,30,78,3,67,60,43,90,23,46,78]
l1=[k*k for k in l if k%2!=0]
print(l1)
# ======================================================================================
'''Replace every even number with 0.'''
l=[1,23,15,46,78,33,56,30,78,3,67,60,43,90,23,46,78]
l1=[0 if k%2==0 else k for k in l]
print(l1)
# ======================================================================================
'''Store only duplicate numbers (duplicates allowed).'''
l=[1,2,4,5,3,2,4,65,7,5,43,2,3,5,78,3,4,7,8]
l1=[k for k in l if l.count(k)>1]
print(l1)
# ======================================================================================
'''TUPLE DATA TYPE'''
# tuple use paranthesis, it is immutable, does not allow add, delete, insert, modify or update elements
# duplicate values are allowed, it is indexed, it is ordered, it is iterable
# inorder to make changes in tuple, convert it into mutable type, i.e., list, b=list(a), a=tuple(b)
# a,b=1,2   a=1, b=2
# ======================================================================================
'''store a single data in a tuple'''
a=('a',)
print(type(a))
# ======================================================================================