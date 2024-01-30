# WAP to print a odd and even numbers between 1 to 20 and find their sum
even = 0
odd = 0
x = 1
while(x<=20):
    if x%2 == 0:
        even+=x
    else:
        odd+=x
    x+=1
print(f"Sum of Even Number is :: {even}")
print(f"Sum of odd Number is :: {odd}")

