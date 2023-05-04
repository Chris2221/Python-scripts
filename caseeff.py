string = input("Enter a string: ")
option = input("Enter 'U' for uppercase or 'L' for lowercase: ")

if option == 'U':
    result = string.upper()
elif option == 'L':
    result = string.lower()
else:
    print("Invalid option")

print(result)
