for x in range(1,51):
    if(x%3 ==0 and x%5 ==0):
        print(f"The Number is - {x} :: 'By_Both'")
    elif(x%5 == 0):
        print(f"The Number is - {x} :: '5_Multiples'")
    elif(x%3 == 0):
        print(f"The Number is - {x} :: '3_Multiples'")


