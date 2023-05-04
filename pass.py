def calculate_total_attempts(days, attempts_per_day, password_length):
    return days * attempts_per_day * password_length ** 4

def years_to_password(password, attempts_per_day):
    password_length = len(password)
    days = 0
    while True:
        days += 1
        total_attempts = calculate_total_attempts(days, attempts_per_day, password_length)
        if total_attempts >= password_length ** 4:
            break
    return days / 365

password = input("Enter password: ")
attempts_per_day = int(input("Enter attempts per day: "))
result = years_to_password(password, attempts_per_day)
print(f"It will take {result:.2f} years to guess the password.")
