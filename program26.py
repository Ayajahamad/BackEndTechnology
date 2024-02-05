# 1. Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.

# firstName = str(input("Enter Your first name :: "))
# lastName = str(input("Enter Your first name :: "))
#
# first = ""
# last = ""
#
# for i in range((len(firstName)-1),-1,-1):
#     first+=firstName[i]
#
# for i in range((len(lastName)-1),-1,-1):
#     last+=lastName[i]
#
# print(f"{first} {last}")

# 2. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# userNumber = str(input("Enter the numbers :: "))
# print(list(userNumber))
# print(tuple(userNumber))

# 3. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.

# number1 = int(input("Enter a first Number :: "))
# number2 = int(input("Enter a second Number :: "))
# number3 = int(input("Enter a third Number :: "))
#
# sum = number1+number2+number3
#
# if(number1==number2==number3):
#     for i in range(0,2):
#         print(sum)
# else:
#     print(sum)

# 4. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# number1 = int(input("Enter a first Number :: "))
# number2 = int(input("Enter a second Number :: "))
# number3 = int(input("Enter a third Number :: "))
#
# sum = number1+number2+number3
#
# if(number1==number2 or number1==number3 or number2==number3):
#     print(0)
# else:print(sum)

# 5. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

# number1 = int(input("Enter a first Number :: "))
# number2 = int(input("Enter a second Number :: "))
# number3 = int(input("Enter a third Number :: "))
#
# sum = number1+number2+number3
#
# if sum>15 and sum<20:
#     print(20)
# else:print(sum)

# 6. Write a Python program that displays your name, age, and address on three different lines.

# name = str(input("Enter your Name :: "))
# age = input("Enter your Age :: ")
# address = input("Enter your Address :: ")
#
# print(name)
# print(age)
# print(address)

# 7. Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49

# x = int(input("Enter the first Number :: "))
# y = int(input("Enter the second Number :: "))
#
# z = x+y
# print(f"OutPut using (x + y) * (x + y) format :: {z**2}")

# 8. Python program to find the largest number in a list without using built-in functions and also find its position.
# Given the list numbers = [3,8,1,7,2,9,5,4]

numbers = [3,8,1,7,2,9,5,4]

# numbers.sort()
# print(numbers[-1])

# Another Method
big = numbers[0]
for i in range(len(numbers)):
    if(numbers[i] > big):
        big = numbers[i]
        position = i
print(f"The largest element is : {big}, Which found at position : {position}")

# 9. Python program to find the sum of the digits of an integer using a while loop
sum = 0
number = int(input("Enter an integer : "))
while(number!=0):
    digit = number%10
    sum = sum+digit
    number = number//10
print("Sum of digits is: ", sum)

# 10. Write a python program to create a Simple Calculator using loop


