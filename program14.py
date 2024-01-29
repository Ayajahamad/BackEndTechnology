number = int(input("Enter a number: "))

result = 1
if number < 0 :
    print("Invalid Input")
else:
    for i in range(1, number + 1):
        # print(i)
        result *= i
    print(f"The factorial of {number} is :: {result}")
