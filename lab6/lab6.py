import re

def validate_name(name):
    return bool(re.match(r"^[A-Za-z\s]+$", name))

def validate_passport_number(passport_number):
    return bool(re.match(r"^[A-Za-z0-9]{9}$", passport_number))

def validate_phone_number(phone_number):
    if (phone_number[0:3] == "+91") :
        return bool(re.match(r"^\d{10}$", phone_number[3:]))
    else : 
        return bool(re.match(r"^\d{10}$", phone_number))

def validate_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email))

def validate_departure_date(departure_date):
    return bool(re.match(r"^\d{2}/\d{2}/\d{4}$", departure_date))

def validate_payment_method(payment_method):
    return bool(re.match(r"^(credit|debit|netbanking)$", payment_method))

def validate_full_date(day, month, year):
    if (month < 1 or month > 12) or (day < 1 or day > 31) or (year < 1000 or year > 9999):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False
    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False
    if month == 2:
        if (year % 4 == 0 and (day < 1 or day > 29)) or (year % 4 != 0 and (day < 1 or day > 28)):
            return False
    return True

while True:
    name = input("Enter your name: ")
    if validate_name(name):
        print("Valid name entered")
        break
    else :
        print("Invalid name! Only alphabetic characters and spaces are allowed.")

while True:
    passport_number = input("Enter your passport number: ")
    if validate_passport_number(passport_number):
        print("Valid passport number entered")
        break
    else : 
        print("Invalid passport number! It must be exactly 9 alphanumeric characters.")

while True:
    phone_number = input("Enter your phone number: ")
    if validate_phone_number(phone_number):
        print("Valid phone number entered")
        break
    else : 
        print("Invalid phone number! It must be exactly 10 digits.")

while True:
    email = input("Enter your email address: ")
    if validate_email(email):
        print("Valid email entered")
        break
    else :
        print("Invalid email address! Please enter a valid email.")

while True:
    departure_date = input("Enter your departure date (dd/mm/yyyy): ")
    if validate_departure_date(departure_date):
        date_parts = departure_date.split('/')
        day = int(date_parts[0])
        month = int(date_parts[1])
        year = int(date_parts[2])
        
        if validate_full_date(day, month, year):
            print("Valid departure date entered")
            break
        else:
            print("Invalid date! Please enter a valid date.")
    else:
        print("Invalid format! Please enter the date in the format dd/mm/yyyy.")

while True:
    payment_method = input("Enter payment method (credit/debit/netbanking): ")
    if validate_payment_method(payment_method):
        print("Valid payment method entered")
        break
    else :
        print("Invalid payment method! It must be either 'credit', 'debit', or 'netbanking'.")

print("All inputs are valid!")
print("Name:", name)
print("Passport Number:", passport_number)
print("Phone:", phone_number)
print("Email:", email)
print("Departure Date:", f"{day}/{month}/{year}")
print("Payment Method:", payment_method)
