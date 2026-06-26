# ==========================================================================================================

'''STRING DATA TYPE'''    # it is ordered and immutable, index starts from 0 (it is a sequence of characters enclosed in single, double or triple quotes)

# ==========================================================================================================
name="liyana"
print(id(name))
name+="kollam"
print(id(name))
# ==========================================================================================================
'''String Indexing'''
name='liyana'
print(name[0])
print(name[3])
print(name[-1])    # index: from left to right 0 to len-1, from right to left -1 to -len
print(name[-5])
# ==========================================================================================================
'''String Concatenation'''
a="hello"
b="world"     # can only add strings with string, not an inetger or float, but integer and float can be operated together and the result will be a float value
print(a+" "+b)
# ==========================================================================================================
num=1
num1="a"
print(str(num)+num1)   # type conversion must be done
# ==========================================================================================================
'''String Repitition'''
word="hi"
print(word*5)    # word*5 = word + word + word + word + word
# ==========================================================================================================
'''String slicing'''   # extractng a part of the string (creating a substring)
text="python"
print(text[1:4])   # yth (starting value is included but ending value is excluded)
# ==========================================================================================================
text="haihello"
print(text[:])   # haihello
print(text[0:])  # haihello
print(text[:6])   # haihel
print(text[1:6:2])   # ahl
print(text[0:100])   # haihello
print(text[1:5])   # aihe
print(text[8:5:-1])   # ol
print(text[5:8:-1])   # no output (since 5-1 will never go upto 8)
print(text[-1:-5:1])   # no output (since -1+1 will never go down to -5)
print(text[-1:-5:-1])   # olle
print(text[::-1])   # ollehiah
print(text[:-1])   # haihell
# ==========================================================================================================
'''Membership operator in String'''
print("py" in "python")
print("java" not in "python")
# ==========================================================================================================
'''Methods applicable to string'''
print(dir(str))
'''['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format',
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 
'title', 'translate', 'upper', 'zfill']'''
# ==========================================================================================================
txt="liYanA IS A programmer"
print(txt.upper())    # convert to uppercase
print(txt.lower())    # convert to lowercase (it is applicable only in standard english language)
print(txt.capitalize())    # convert first letter of the first word of a sentence to uppercase
print(txt.title())    # convert first letter of each word in a sentence to uppercase
print(txt.casefold())    # convert to lowercase, it works with every languages
print(txt.swapcase())    # convert lower to uppercase and upper to lower
print(txt.find("i"))    # returns the index position
print(txt.find("A"))    # returns the first "A"s index position
print(txt.find("z"))    # if no character is found then returns -1 as the index position (it means there is no character in the string)
print(txt.find("mm"))    # if "mm" is found, the index of first "m" is returned
print(txt.index("g"))    # if character is found, returns the index position
print(txt.index("z"))    # if character is not found, returns error
# ==========================================================================================================
name="  liyana  "
print(name)
print(name.strip())   # no whitespace (strips both left and right whitespace of the string)
print(name.lstrip())    # strips left whitespace of the string
print(name.rstrip())    # strips right whitespace of the string
# ==========================================================================================================
txt="beautiful"
txt1="beautiful1234"
print(txt.isalpha())    # true (returns true is the string is an alphabetic string else returns false)
print(txt1.isalpha())   # false
print(txt.isdigit())      # false
print(txt1.isdigit())     # false
txt2="24356"
print(txt2.isdigit())     # true (returs true if a string is a digit string)
print(txt.isalnum())      # true (checks whether the string contains character or numbers or combination)
print(txt1.isalnum())     # true
print(txt2.isalnum())     # true
txt="123.556"
print(txt.isdecimal())   #f alse cuz of special character "."   (Returns True only if all characters are decimal numbers.)
print(txt.isdigit())     #false   (Returns True for digits including superscript digits.)
print(txt.isnumeric())   #false   (Returns True for anything Python recognizes as numeric.)
'''isdecimal() ⊂ isdigit() ⊂ isnumeric()'''
# ==========================================================================================================
word="werewerrertrefgdsdvcxzzxcsdfgddfdgzxcvbncxzzzzzzzzzzxcv"
print(word.count("z"))
# ==========================================================================================================
word="drswfyaGH TEFD EHU EW"
print(word.encode())
# ==========================================================================================================
word="i am from wayanad"
print(word.endswith("ad"))
print(word.endswith("rt"))
# ==========================================================================================================
'''format, "f" using {}'''
# ==========================================================================================================
a="rtyu"
b="<ey$你好*"
print(a.isascii())
print(b.isascii())
print(ord("A"))   # to get ascii value, ord() is used
# ==========================================================================================================
a={"anu","miya","kiya"}
b=["dfg","rty","wer"]
print("@".join(a))
print("@".join(b))
# ==========================================================================================================
word="python is easy and is free"
print(word.replace("is","*"))
print(word)
# ==========================================================================================================
word="python is easy and is free"
print(word.split())  # default condition is taken as whitespace and splitting will be done form left by deafult
print(word.split('i'))
a="blue,red,pink"
print(a.rsplit(','))
print(a.rsplit('e'))
# ==========================================================================================================l;