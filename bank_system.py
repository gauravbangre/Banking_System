import re

def generate_account_number():
    from random import randint
    return f"{randint(1000000000, 9999999999)}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added to the bank.")

    def remove_customer(self, customer):
        self.customers.remove(customer)

class Customer:
    def __init__(self, name, father_name, mother_name, surname, email, address, phone, aadhaar, pan, balance, dob):
        self.name = name
        self.father_name = father_name 
        self.mother_name = mother_name
        self.surname = surname
        self.email = email
        self.address = address
        self.phone = phone
        self.aadhaar = aadhaar
        self.pan = pan
        self.balance = balance
        self.dob = dob
        self.account_number = generate_account_number()
        self.debit_card = None
        self.credit_card = None

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            return self.balance

    def borrow(self, amount):
        self.balance += amount
        print("Your Acc. Balance is:", self.balance)

    def view_details(self, acc_no, dob):
        if self.account_number == acc_no and self.dob == dob:
            print("Account Number:", self.account_number)
            print("Name:", self.name)
            print("Father's Name:", self.father_name)
            print("Mother's Name:", self.mother_name)
            print("Surname:", self.surname)
            print("Email:", self.email)
            print("Address:", self.address)
            print("Phone:", self.phone)
            print("Aadhaar Number:", self.aadhaar)
            print("PAN Number:", self.pan)
            print("Balance:", self.balance)
            print("Debit Card:", self.debit_card)
            print("Credit Card:", self.credit_card)
        else:
            print("Account not found or details do not match!")

    def edit_details(self):
        print("1. Name")
        print("2. Father's Name")
        print("3. Mother's Name")
        print("4. Surname")
        print("5. Email")
        print("6. Address")
        print("7. Phone")
        print("8. Aadhaar Number")
        print("9. PAN Number")
        choice = int(input("Enter the field number you want to edit: "))
        if choice == 1:
            self.name = input("Enter new name: ")
        elif choice == 2:
            self.father_name = input("Enter new father's name: ")
        elif choice == 3:
            self.mother_name = input("Enter new mother's name: ")
        elif choice == 4:
            self.surname = input("Enter new surname: ")
        elif choice == 5:
            self.email = input("Enter new email: ")
        elif choice == 6:
            self.address = input("Enter new address: ")
        elif choice == 7:
            self.phone = input("Enter phone number: ")
            while not (self.phone.isdigit() and len(self.phone) == 10):
                self.phone = input("Invalid phone number. Enter 10-digit phone number: ")
        elif choice == 8:
            self.aadhaar = input("Enter Aadhaar number: ")
            while not (self.aadhaar.isdigit() and len(self.aadhaar) == 12):
                self.aadhaar = input("Invalid Aadhaar number. Enter 12-digit Aadhaar number: ")
        elif choice == 9:
            self.pan = input("Enter new PAN number: ")
            while not (len(self.pan) == 10):
                self.pan = input("Invalid PAN number. Enter correct PAN number: ")
        else:
            print("Invalid choice")

    def delete_account(self):
        self.name = ""
        self.father_name = ""
        self.mother_name = ""
        self.surname = ""
        self.email = ""
        self.address = ""
        self.phone = ""
        self.aadhaar = ""
        self.pan = ""
        self.balance = 0
        self.account_number = ""
        print("Account deleted successfully!")

    def assign_debit_card(self):
        self.debit_card = f"DEBIT-{self.account_number[-4:]}-{generate_account_number()[-4:]}"
        print(f"Debit card assigned: {self.debit_card}")

    def assign_credit_card(self):
        self.credit_card = f"CREDIT-{self.account_number[-4:]}-{generate_account_number()[-4:]}"
        print(f"Credit card assigned: {self.credit_card}")

bank = Bank(" Banking System ")

while True:
    print("\n*--------------------- Welcome to Banking System -----------------------*")
    print("::::::::::::::Menu options for below Operation (Select between 1-8)::::::::::")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Borrow")
    print("5. View details")
    print("6. Edit details")
    print("7. Remove account")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter Your First Name: ")
        father_name = input("Enter Father's Name: ")
        mother_name = input("Enter Mother's Name: ")
        surname = input("Enter your Surname: ")
        email = input("Enter your Valid email: ")
        address = input("Enter address: ")
        phone = input("Enter phone number: ")
        while not (phone.isdigit() and len(phone) == 10):
            phone = input("Invalid phone number. Enter 10-digit phone number: ")
        aadhaar = input("Enter Aadhaar number: ")
        while not (aadhaar.isdigit() and len(aadhaar) == 12):
            aadhaar = input("Invalid Aadhaar number. Enter 12-digit Aadhaar number: ")
        pan = input("Enter new PAN number: ")
        while not (len(pan) == 10):
            pan = input("Invalid PAN number\nEnter correct PAN number: ")
        balance = float(input("Enter initial balance: "))
        dob = input("Enter date of birth (YYYY-MM-DD): ")

        customer = Customer(name, father_name, mother_name, surname, email, address, phone, aadhaar, pan, balance, dob)
        bank.add_customer(customer)
        print("Customer account created successfully!")
        print("Your Account Number is:", customer.account_number)

        card_choice = input("Do you want a debit card (yes/no)? ").strip().lower()
        if card_choice == 'yes':
            customer.assign_debit_card()

        card_choice = input("Do you want a credit card (yes/no)? ").strip().lower()
        if card_choice == 'yes':
            customer.assign_credit_card()

    elif choice == 2:
        aadhaar = input("Enter Aadhaar number: ")
        acc_no = input("Enter Account Number: ")
        for customer in bank.customers:
            if customer.aadhaar == aadhaar and customer.account_number == acc_no:
                amount = float(input("Enter amount to deposit: "))
                customer.deposit(amount)
                print("Amount deposited successfully!")
                print("Customer Balance:", customer.balance)
                break
        else:
            print("Customer not found")

    elif choice == 3:
        acc_no = input("Enter Account Number: ")
        for customer in bank.customers:
            if customer.account_number == acc_no:
                amount = float(input("Enter amount to withdraw: "))
                customer.withdraw(amount)
                print("Amount withdrawn successfully!")
                print("Customer Balance:", customer.balance)
                break
        else:
            print("Customer not found")

    elif choice == 4:
        acc_no = input("Enter Account Number: ")
        for customer in bank.customers:
            if customer.account_number == acc_no:
                amount = float(input("Enter amount to borrow: "))
                customer.borrow(amount)
                print("Amount borrowed successfully!")
                break
        else:
            print("Customer not found")

    elif choice == 5:
        acc_no = input("Enter Account Number: ")
        dob = input("Enter date of birth (YYYY-MM-DD): ")
        for customer in bank.customers:
            if customer.account_number == acc_no and customer.dob == dob:
                customer.view_details(acc_no, dob)
                break
        else:
            print("Customer not found or details do not match!")

    elif choice == 6:
        acc_no = input("Enter Account Number: ")
        for customer in bank.customers:
            if customer.account_number == acc_no:
                customer.edit_details()
                break
        else:
            print("Customer not found")

    elif choice == 7:
        acc_no = input("Enter Account Number: ")
        for customer in bank.customers:
            if customer.account_number == acc_no:
                customer.delete_account()
                bank.remove_customer(customer)
                break
        else:
            print("Customer not found")

    elif choice == 8:
        print("Thank you for banking with MV Banking System")
        break

    else:
        print("Invalid Choice")
        print("Enter number between 1-8")
