# Membership opeartor
# in - not in
print("Membership opeartor")
a = "Python operators"
b = {1,'x',2.0,'y'}

print("P" in a)
print("p" in a)

print("python" not in a)

print(1 in b)

print('y' in b)

# Identity Operator
print("Identity Operator")
a1 = 3
b1 = 3
a2 = "Python"
b2 = "python"

a3 = [4,5,6]
b3 = [4,5,6]

print(a1 is not b1)
print(a2 is not b2)
print(a3 is b3)


# Type Conversion (implicit & explicit)

s = "10000"

print(" Before Conversion :: ")
print(s)
print(type(s))

print("After converting to Int ::")
s1 = int(s)
s3 = int(s,2)
print(s1)
print(type(s1))
print(s3)

print("After converting to Float ::")
s2 = float(s)
print(s2)
print(type(s2))

print("List Accessing ::")
my_list = ['p', 'q', 'r', 's', 't', 'u']
subjects = ['maths', 'science', 'social', ['kannada', 'english', 'hindi'], 'sankriti']
print(subjects[3][2])

# first item
print(my_list[0])

# third item
print(my_list[2])

# fifth item
print(my_list[4])

# Negative Indexing in List

# List Slicing in Python
print("List Slicing in Python :: ")

my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print(len(my_list))
print(my_list[2:5])

print(my_list[5:])
print(my_list[:])
print(my_list[:5])
print(my_list[:-5])

# Adding values in list (overlaping)
print("Adding values in list (overlaping) :: ")
even = [2,4,6,8,10]
even[0] = 1
print(even)
even[1:] = 3,5,7,9;
print(even)

# append nad extend in list
print("append and extend in list :: ")

even = [2,4,6,8,10]

even.append([1,3,5,7,9])
print(even)

even.extend([1,3,5,7,9])
print(even)

# Delete list
print("Delete list :: ")
delete = [2,4,6,8,10]
print(delete)
# del , pop(), remove(), clear()

# Sorting in list
print("Sorting in list :: ")
myList = [34,56,34,12,32,1,12,34,56,54]
myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

# dir(anyListName) - shows all the operation about list

