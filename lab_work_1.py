<<<<<<< HEAD

numbers = [5, 10, 3, 8, 2, 7, 6, 1, 4, 9]
total = 0

for num in numbers:
    total += num

print("The sum of the numbers is:", total)
=======
# Lab Work 1 - Weird Number Checker

# Collect user input
n = int(input("Enter an integer: "))

# Check the conditions
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
>>>>>>> 58b033ad7d5aa6765c577abf71cf928fd34bdc7a
