carChargeP_H = 5000.0
bikeChargeP_H = 500.0

tax_rate = 0.1

vehicle_type = input("Enter the vehicle type (car/bike): ")

rental_hours = int(input("Enter the number of hours rented: "))

if vehicle_type == "car":
    total_charge = carChargeP_H * rental_hours
elif vehicle_type == "bike":
    total_charge = bikeChargeP_H * rental_hours
else:
    print("Invalid vehicle type.")
    total_charge = 0

tax_amount = total_charge * tax_rate

total_amount = total_charge + tax_amount

print("\nInvoice Details:")
print(f"Vehicle Type: {vehicle_type}")
print(f"Rental Hours: {rental_hours} hours")
print(f"Tax Amount: {tax_amount} ")
print(f"Total Amount: {total_amount} ")


