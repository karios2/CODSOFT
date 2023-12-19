import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == '1' and computer_choice == '3') or
        (user_choice == '2' and computer_choice == '1') or
        (user_choice == '3' and computer_choice == '2')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_round():
    print("Choose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_choice = input("Enter 1, 2, or 3: ")

    if user_choice not in ['1', '2', '3']:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return play_round()

    user_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}[user_choice]
    
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)

    print(f"\nYour choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    return result

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"\nScores - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()
