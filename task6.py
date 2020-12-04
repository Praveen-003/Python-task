# question 1-add +2 to every value to element in list
lst = []
n = int(input("enter the size of the list"))
print("enter the elements")
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in range(0, n):
    lst[i] += 2
print(lst)



# question 2-to get given pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()
print("")


#question 3 -fibonacci sequence
n = int(input("Enter the number for fibonacci series:"))
f = 0
s = 1
print("The fibonacci series:-")
print(f, end=' ')
for i in range(1, n):
    t = s
    s = s + f
    f = t
    print(t, end='  ')
print('\n')

#question 4-armstrong number
n = int(input("Enter the number to check the number is armstrong r not:"))
t = n
s = 0
while t > 0:
    r = t % 10
    s += r ** 3
    t //= 10
if n == s:
    print(n, "is a armstrong number")
else:
    print(n, "is not a armstrong number")
print('\n')

# question 5-tables
num = 9
n = int(input("tills:"))
for i in range(1, n):
    print(num, 'x', i, '=', num*i)




# question 6 postive or negative
N = int(input("ENTER THE NUMBER:-"))
if(N<0):
    print("THE NUMBER IS NEGATIVE...")
elif(N>0):
    print("THE NUMBER IS POSITIVE...")
else:
    print("THE NUMBER IS ZERO...")

#question 7- convert number of days to age
n = int(input("Enter the number of days :"))
age = n // 365
print("The age is", age)
print('\n')

#question 8-trigonomentry function
import math
n = int(input("Enter the degree:"))
val = math.radians(n)
print("Enter the function need to find trigonomentry(sin,cos,tan,asin,acos,atan,sinh,cosh,tanh):")
print("=>")
func=input()
if func == "sin":
    print("Sine of", n, "is", math.sin(val))
else:
    if func == "cos":
        print("Cosine of", n, "is", math.cos(val))
    else:
        if func == "tan":
            print("Tangent of", n, "is", math.tan(val))
        else:
            if func == "asin":
                print("Inverse of sine ", n, "is", math.asin(val))
            else:
                if func == "acos":
                    print("Cosine Inverse of", n, "is", math.acos(val))
                else:
                    if func == "atan":
                        print("Inverse of Tangent ", n, "is", math.atan(val))
                    else:
                        if func == "sinh":
                            print("Hyperbolic Sine of", n, "is", math.sinh(val))
                        else:
                            if func == "cosh":
                                print("Hyperbolic Cosine of", n, "is", math.cosh(val))
                            else:
                                if func == "tanh":
                                    print("Hyperbolic Tangent of", n, "is", math.tanh(val))
                                else:
                                    print("Error:Invalid function")
        print('\n')



# question-9 calculator

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("select operation")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.divide")
choice = int(input("enter the choice(1/2/3/4)"))
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
    print(num1, "-", num2, "=", sub(num1, num2))
elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("invalid input")