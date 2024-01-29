month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

if month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid input.")
else:
    if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day < 21):
        season = "Spring"
    elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day < 23):
        season = "Summer"
    elif (month == 9 and day >= 23) or (month > 9 and month < 12) or (month == 12 and day < 21):
        season = "Fall"
    else:
        season = "Winter"

    print(f"The season for {month}/{day} is {season}.")
