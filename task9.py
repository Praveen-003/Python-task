#multiply of x and y by lamba
n = lambda x, y: x * y
a = int(input("Enter the two number:"))
b = int(input())
print("The multiple of", a, "and", b, "is", n(a, b))
print('\n')



#fibonacci series to n

f = lambda x, y: x + y
n = int(input("Enter the number:"))
a = 0
b = 1
print(a)
for i in range(1, n):
    t = b
    b = f(a, b)
    a = t
    print(a)
print('\n')


#multiples each number by given number
lst = [45, 36, 19, 24, 60, 18]
a = 4
print("Original List:", lst)
print("Given number:", a)
res = list(map(lambda x: x*a, lst))
print(' '.join(map(str, res)))
print('\n')



#find number divisible by 9 from a list
print("Original List:", lst)
ls = list(filter(lambda x: (x % 9 == 0), lst))
print("Result:", ls)
print('\n')


#to count number of even number in the list
lst = [45, 62, 36, 15, 81]
print("Original List:", lst)
ls = list(filter(lambda x: (x % 2 == 0), lst))
print("Result:", len(ls))
print('\n')
