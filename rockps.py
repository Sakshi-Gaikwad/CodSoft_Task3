import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def print_choices(user_choice, computer_choice):
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # User input
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Validate user input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer generates a random choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Determine the winner and display the result
    result = determine_winner(user_choice, computer_choice)
    print_choices(user_choice, computer_choice)
    print(result)

    # Update scores
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    # Display current scores
    print(f"Your score: {user_score}, Computer score: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
