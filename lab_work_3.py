total = 0

while True:
    number = int(input("Enter a number (negative to stop): "))
    if number < 0:
        break
    total += number

print("The sum of all entered numbers is:", total)
