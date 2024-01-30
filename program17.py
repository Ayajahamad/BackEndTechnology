# Factorial of a given Number

number = int(input("Enter a number: "))

fib = 1;
result = 1
if number < 0 :
    print("Invalid Input")
else:
    while(result <= number):
        fib*=result
        result+=1
    print(fib)
