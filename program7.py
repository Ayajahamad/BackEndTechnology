bank_accounts = {
    1: {"owner_name": "Faisal","acc_type":"saving", "balance": 1000.0,"bank_name":"KVGB"},
    2: {"owner_name": "Sajjad S","acc_type":"current", "balance": 500.0,"bank_name":"SBI"},
}

entered_id = int(input("Enter your account ID: "))

if entered_id == 1:
    print("\nAccount Information:")
    print(f"Account ID: {entered_id}")
    print(f"Owner Name: {bank_accounts[entered_id]['owner_name']}")
    print(f"Bank Name :: {bank_accounts[entered_id]['bank_name']}")
    print(f"Account Type {bank_accounts[entered_id]['acc_type']}")
    print(f"Balance: ${bank_accounts[entered_id]['balance']}")
    deposit = int(input(f"Enter Amount You Want to Deposit :: "))
    total = (deposit) + (bank_accounts[entered_id]['balance'])
    print(f"Total Amount is : {total}")
    print(f"Deposit Amount Is {deposit}")
    credit = int(input(f"Enter Amount You Want to credit :: "))
    print(f"Credited Amount Is {credit}")
    print(f"After Credited Total Amount is : {(total)-(credit)}")
elif entered_id == 2:
    print("\nAccount Information:")
    print(f"Account ID: {entered_id}")
    print(f"Owner Name: {bank_accounts[entered_id]['owner_name']}")
    print(f"Bank Name :: {bank_accounts[entered_id]['bank_name']}")
    print(f"Account Type {bank_accounts[entered_id]['acc_type']}")
    print(f"Balance: ${bank_accounts[entered_id]['balance']}")
    deposit = int(input(f"Enter Amount You Want to Deposit :: "))
    total = (deposit) + (bank_accounts[entered_id]['balance'])
    print(f"Total Amount is : {total}")
    print(f"Deposit Amount Is {deposit}")
    credit = int(input(f"Enter Amount You Want to credit :: "))
    print(f"Credited Amount Is {credit}")
    print(f"After Credited Total Amount is : {(total)-(credit)}")
else:
    print("Account not found.")
