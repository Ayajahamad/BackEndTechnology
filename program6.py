bp = float(input("Enter Basic Pay: "))
hra = float(input("Enter House Rent Allowance (HRA): "))
ta = float(input("Enter Travel Allowance (TA): "))
da = float(input("Enter Dearness Allowance (DA): "))

total_salary = bp + hra + ta + da

if (total_salary >= 50000):
    designation = "Manager"
elif (total_salary >= 30000) & (total_salary <= 50000):
    designation = "Assistant Manager"
elif (total_salary >= 15000) & (total_salary <= 30000):
    designation = "Executive"
else:
    designation = "Trainee"

print(f"Total Salary is - {total_salary} and Designation is - {designation}")

