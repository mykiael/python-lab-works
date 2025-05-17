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
