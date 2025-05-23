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
