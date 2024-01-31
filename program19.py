# WAP to find the multiples of 3 and 5 between 1 to 50 and if the number is divisible by 3 then display 3_Multiples if the number devisible by 5 then display the result as 5_multiple if both then display the result as by Both
# Using While Loop

x = 1
while(x<=50):
    if(x%3==0 and x%5 == 0):
        print(f"Number {x} :: 'By_Both'")
    elif(x%3==0):
        print(f"Number {x} ::  'By_3'")
    elif(x%5==0):
        print(f"Number {x} ::  'By_5'")
    x+=1
