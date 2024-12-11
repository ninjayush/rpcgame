import random

choices = ["r", "p", "s"]

def winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "r" and computer_choice == "s") or \
            (player_choice == "s" and computer_choice == "p") or \
            (player_choice == "p" and computer_choice == "r"):
        return "You win!"
    else:
        return "You lose!"

def rpc():
    print("Welcome to Rock-Paper-Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

    while True:
        player_choice = input("Your choice: ").strip().lower()

        if player_choice == "q":
            print("Thanks for playing!")
            break
        elif player_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = winner(player_choice, computer_choice)
        print(result)
        print()

rpc()

#done