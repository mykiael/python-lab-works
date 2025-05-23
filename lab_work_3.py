<<<<<<< HEAD
total = 0

while True:
    number = int(input("Enter a number (negative to stop): "))
    if number < 0:
        break
    total += number

print("The sum of all entered numbers is:", total)
=======
# Lab Work 3 - Simple Quiz Game

# Introduction
print("Welcome to the Quiz Game!")

# Score tracker
score = 0

# First question
answer1 = input("What is the capital of Nigeria? ").strip().lower()
if answer1 == "abuja":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Abuja.")

# Second question
answer2 = input("Which programming language are you learning? ").strip().lower()
if answer2 == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Python.")

# Third question
answer3 = input("What is 2 + 2? ").strip()
if answer3 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 4.")

# Show the final score
print(f"Your final score is {score} out of 3. Thanks for playing!")
>>>>>>> 58b033ad7d5aa6765c577abf71cf928fd34bdc7a
