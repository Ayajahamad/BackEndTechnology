# Palindrom of a given Number

num = int(input("Enter the number :: "))
rev = 0
temp = num
while(num!=0):
    digit = num % 10
    rev = rev*10+digit
    num//=10
print(f"The reverse of the Number is :: {rev}")
if(rev == temp):
    print("Entered Number is a Palindrom")
else:
    print("Entered Number is Not a Palindrom")
