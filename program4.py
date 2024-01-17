# # Tuples
# print("Tuples :: ")
a = (1,2,3,4,5)
#
#
# print(type(a))
#
# print(len(a))
#
# b = (1,2,3,5,[3,4,5,6],'be-practical',34.23,(9,8,7))
# print(b)
# c = b[4][2] = 25
# print(c)
# print(b)
#
# print("--------------------------------------")
# print("Zip the Tuple :: ")
#
# first_names = ('Anil','Sarah','Mehta','Arjun')
# last_names = ('Narang','Smith','Raj','Gowda')
# ages = (49,55,39,33)
#
# res = zip(first_names,last_names,ages)
# print(res)
#
# print("-----------------------------")
#
# customers = tuple(res)
# print(customers)
#
# print(f"first name last name is {customers[2][0]} {customers[2][1]} and his age is {customers[2][2]}")
#
# print("-------------------------------Another Way")
# first_names,last_names,ages = customers[2]
# print(f"First name last name is {first_names} {last_names} and his age is {ages} ")
#
# u = sorted(customers)
# print(u)
#
# print("--------------------------------------------------- SET")
#
# mySet = {'apple','banana','orange'}
# print(type(mySet))
#
# mySet.add("cherry")
# print(mySet)
#
# mySet.update(['cherry','durry','burry'])
# print(mySet)
#
# myset = {3,5,2,3,1,4,6,2,3,'a','s','d'}
# print(myset)
# print(type(mySet))
#
# print("Frozen Set------------------------------------------")
# froSet = {3,5,2,3,1,4,6,2,3,'a','s','d'}
# frozenset(froSet)
# print(froSet)
