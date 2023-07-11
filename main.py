import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    choices = ["rock", "paper", "scissors"]
    while True:
        print("Rock, Paper, Scissors - Make your choice:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("0. Quit")
        player_choice = input("Enter your choice (0-3): ")
        
        if player_choice == "0":
            print("Thanks for playing. Goodbye!")
            break
        
        if player_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue
        
        player_choice = choices[int(player_choice) - 1]
        computer_choice = random.choice(choices)
        
        print("You chose:", player_choice)
        print("Computer chose:", computer_choice)
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        print()

# Start the game



--
