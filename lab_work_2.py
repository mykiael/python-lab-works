<<<<<<< HEAD
import random


secret_number = random.randint(1, 10)


for attempt in range(5):
    guess = int(input("Guess the secret number (1 to 10): "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right.")
        break
    else:
        print("❌ Wrong guess, try again.")


else:
    print("😢 Sorry, you’ve used all 5 guesses. The number was", secret_number)
=======
# Lab Work 2 - House Downpayment Calculator

# Fixed price of the house
house_price = 1000000

# Get the user's budget
user_budget = int(input("Enter your house budget: "))

# Calculate downpayment based on the budget
if 300000 < user_budget < 500000:
    downpayment = (10 / 100) * house_price
    print(f"Your downpayment is 10%: ₦{downpayment}")
elif user_budget >= 500000:
    downpayment = (20 / 100) * house_price
    print(f"Your downpayment is 20%: ₦{downpayment}")
else:
    print("Your budget is too low for this house.")
>>>>>>> 58b033ad7d5aa6765c577abf71cf928fd34bdc7a
