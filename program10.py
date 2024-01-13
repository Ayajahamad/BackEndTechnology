# WAP to print a odd and even numbers between 1 to 20 and find their sum
# WAP to find the multiples of 3 and 5 between 1 to 50 and if the number is divisible by 3 then display 3_Multiples if the number devisible by 5 then display the result as 5_multiple if both then display the result as by Both
y = 0;
for x in range(1,20,2):
    print(x)
    y+=x
print(f"Sum Of Odd Numbers From 1 to 20 is :: {y}")

for x in range(2,20,2):
    print(x)
    y+=x
print(f"Sum Of Even Numbers From 1 to 20 is :: {y}")
