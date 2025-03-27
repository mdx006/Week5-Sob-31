import random

def compare_numbers(number, user_guess):
    """Compare the generated number with the user's guess and return (cows, bulls)."""
    cows = 0  # Right digit, wrong place
    bulls = 0  # Right digit, right place

    for i in range(len(number)):  # Compare each digit
        if user_guess[i] == number[i]:
            bulls += 1
        elif user_guess[i] in number:
            cows += 1

    return cows, bulls  # Return tuple (cows, bulls)

playing = True  # Start the game
number = str(random.randint(0, 9999)).zfill(4)  # Generate a random 4-digit number with leading zeros if needed
guesses = 0

print("Let's play a game of Cowbull!")  
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in the wrong place, you get a cow.")
print("For every number in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.")

while playing:
    user_guess = input("Give me your best 4-digit guess: ").zfill(4)  # Ensure 4-digit input
    
    if user_guess.lower() == "exit":
        print("Thanks for playing! The number was", number)
        break

    if not user_guess.isdigit() or len(user_guess) != 4:
        print("Please enter a valid 4-digit number.")
        continue

    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1

    print(f"You have {cowbullcount[0]} cows and {cowbullcount[1]} bulls.")

    if cowbullcount[1] == 4:
        print(f"You win the game after {guesses} guesses! The number was {number}.")
        playing = False  # Stop the game
    else:
        print("Your guess isn't quite right, try again.")
