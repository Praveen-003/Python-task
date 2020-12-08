#Merge a two list using zip
lst1 = ["Dhoni", "Raina", "Jaddu", "Klrahul", "Nattu"]
lst2 = ["Rohit", "Kohli", "Pandya", "Bumrah", "Chahal"]
print("Original List 1:", lst1)
print("Original List 2:", lst2)
print()
x = list(zip(lst1, lst2))
print("Result :", x, sep='\n')
print('\n')


#merge a given list and the range list
lst3 = []
for i in range(1, 8):
    lst3.append(i)
print("Range List:", lst3)
print("Given List:", lst1)
x = list(zip(lst1, lst3))
print("Result:")
print(x)
print('\n')



#sort ascending order
print("Original List:", lst1)
lst1.sort()
print("Result:", lst1)
print('\n')


#fliter function to fliter odd number
def fun(v):
    if v % 2 == 0:
        return False
    else:
        return True
 lst = [23, 36, 885, 94, 15, 672, 95, 267, 24]
flt = filter(fun, lst)
print("Result:")
for i in flt:
    print(i, end=' ')
print()
