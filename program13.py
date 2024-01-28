numbers = (1, 2, 3, 4, 5, 6, 8, 5, 34, 23, 45, 55, 67, 87, 34, 23)

even_count = 0
odd_count = 0

even_sum = 0
odd_sum = 0

for x in numbers:
    if x % 2 == 0:
        even_count += 1
        even_sum += x
    else:
        odd_count += 1
        odd_sum += x

print("Number of even numbers:", even_count)
print("Sum of even numbers:", even_sum)
print("Number of odd numbers:", odd_count)
print("Sum of odd numbers:", odd_sum)
