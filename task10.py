#check a string containing only certain set(a-z.A-Z,0-9)
import re
st = "I like 234to work with ab python3"
print("Original string:", st, sep='\n')
print()
x = re.findall("[a-zA-Z0-9]", st)
print(x)
print()



#that matches a word containing 'ab'
x = re.search('ab*?', st)
if x:
    print("Yes,ab is present in the given string")
else:
    print("No,ab is not present in the given string")
print()



#check number at end of the word r sentences
x = re.findall(r'[0-9]\b', st)
print(x)
if x:
    print("Yes,the string end with a number")
else:
    print("No,the string does not end with a number")
print()


#to search the number of length btn 1 to 3 in a given string
x = re.findall(r'\b[0-9][0-9][0-9]', st)
print(x)
if x:
    print("Yes,the number[0-9] length between 1 to 3 is present in a given string")
else:
    print("No,the number[0-9] lehgth between 1 to 3 is not present in a given string")
print()


#to match a string that contain only upper case
x = re.findall('[A-Z]', st)
print(x)
