import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Rock, Paper, Scissors Game!")
    choices = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if player_choice == "quit":
            print("Thanks for playing!")
            break
        elif player_choice not in choices:
            print("Invalid choice. Try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        result = get_winner(player_choice, computer_choice)
        print(result)

if _name_ == "_main_":
    main()