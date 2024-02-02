# 1) Write a Python program to count the  number of even and odd numbers in a series of  Numbers.

# even = 0
# odd = 0
# numbers = (1,2,3,4,5,6,3,21,7,38,9)
#
# for num in numbers:
#     if num%2 == 0:
#         even+=1
#     else:
#         odd+=1
# print(f"Even Numbers in teh list :: {even}")
# print(f"Odd Numbers in teh list :: {odd}")

# 2) Write a Pyhthon program that prints each item and its corresponding datatype from the following list.

# datalist = [1452,11.23,True,'Be-Practical',(0,-1),[5,12],{"class":'V',"Section":'A'}]
#
# for lst in datalist:
#     print(f"Item :: {lst} => Type of Item is :: {type(lst)}")

# 3) Write a python program that prints all the numbers from 0 to 6 except 3 and 6
#
# i = 0
# for i in range(7):
#         if i%3 != 0:
#             print(i)

# Another Way --

# i = 0
# for i in range(7):
#         if i ==3:
#             continue
#         if i ==6:
#             continue
#         print(i)

# 4) Write a Python program to construct the following pattern. using a nested loop number.

# for x in range(1,5):
#     for y in range(1,x+1):
#         print(x,end =" ")
#     print()

# 5) Write a Python program to multiply all the numbers in a list.

# mul = 1
# list = (8,2,3,-1,7)
# for i in list:
#     mul*=i
# print(mul)

# 6) Write a python program to create and print a list where the values are the square of numbers between 1 and 10.

# for i in range(1,11):
#     print(i**2)

# 7) Write a python program that takes a list and returns a new list with unique elements from the first list.

# list = [1,2,3,3,3,3,4,5]
# nlst = []
# for i in list:
#     if i not in nlst:
#         nlst.append(i)
# print(nlst)

# Another Method

# lst = [1,2,3,3,3,3,4,5]
# a = set(lst)
# b = list(a)
# print(b)


