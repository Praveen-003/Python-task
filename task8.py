#bulid in exception
import sys
try:
    b = 0
    c = 1/int(b)
except (TypeError, ZeroDivisionError):
    print("Error:", sys.exc_info()[0])
try:
    b = 'a'
    c = int(b)
except ValueError:
    print("Error:", sys.exc_info()[0])
try:
    import a
except ImportError:
    print("Error:", sys.exc_info()[0])
try:
    print(x)
except NameError:
    print("Error:", sys.exc_info()[0])
try:
    lst = [2, 25, 41]
    print(lst[4])
except IndexError:
    print("Error:", sys.exc_info()[0])
try:
    import math
    print(math.length())
except AttributeError:
    print("Error:", sys.exc_info()[0])
finally:
    print("Try and except is finished")
print('\n')


#Simple calculator
try:
    m = input("Enter the two operand:")
    n = input()
    a = float(m)
    b= float(n)
except ValueError:
     print("Error:", sys.exc_info()[0])
print("+  -  *  /")
f = input("ENTER THE OPERATION:")
if (f == '+'):
    print("Addition of", a, "and", b, "is", a+b)
else:
    if (f == '-'):
        print("Subtraction of", a, "and", b, "is", a-b)
    else:
        if (f == '*'):
            print("Multiplication of", a, "and", b, "is", a*b)
        else:
            if (f == '/'):
                try:
                   print("Division of", a, "and", b, "is", a/b)
               except ZeroDivisionError:
                   print("Error:", sys.exc_info()[0])
    else:
        print("Error:Invalid Operation")
print('\n')

#raise Exception
try:
    print(x)
    a = b/0
    raise Exception("Error:b cannot divided by 0")
except NameError:
      print("Error:", sys.exc_info()[0])