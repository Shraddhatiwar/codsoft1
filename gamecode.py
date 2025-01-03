import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors (or 'quit' to exit)")
    
    # List of possible choices
    choices = ["rock", "paper", "scissors"]
    
    while True:
        # Get user input
        my_choice = input("Your choice: ").lower()
        
        # Exit condition
        if my_choice == "quit":
            print("Thanks for playing! Goodbye!")
            break
        
        # Validate input
        if my_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
        # Determine the winner
        if my_choice == computer_choice:
            print("It's a tie!")
        elif (my_choice == "rock" and computer_choice == "scissors") or \
             (my_choice == "paper" and computer_choice == "rock") or \
             (my_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")
        
        print()  # Blank line for spacing

# Run the game
play_game()
