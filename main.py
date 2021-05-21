
import random

print("**********************************")
print("   WELCOME TO HUNTER NINJA BEAR")
print("**********************************")
print("  Face-off against the computer ")
print("    where you choose either a  ")
print("    Hunter, Ninja or a Bear ")
print("**********************************")
print("          HOW TO PLAY")
print("**********************************")
print("        Hunter kills Bear")
print("        Bear mauls Ninja")
print("     Ninja karate chops Hunter")
print("**********************************")

while True:
    user_score = 0
    computer_score = 0
    print()
    user_action = input("Hunter, Ninja or Bear): ")
    possible_actions = ["Hunter", "Ninja", "Bear"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action.lower() == computer_action.lower():
        print(f"Both players selected {user_action}, play again!")
    elif user_action.lower() == "Hunter":
        if computer_action.lower() == "Bear":
            print("Hunter kills Bear! You win!")
            user_score = user_score + 1
        else:
            print("Ninja karate chops Hunter! You lose.")
            computer_score = computer_score + 1
    elif user_action.lower() == "Ninja":
        if computer_action.lower() == "Hunter":
            print("Ninja karate chops Hunter! You win!")
            user_score = user_score + 1
        else:
            print("Bear mauls Ninja! You lose.")
            computer_score = computer_score + 1
    elif user_action.lower() == "Bear":
        if computer_action.lower() == "Ninja":
            print("Bear mauls Ninja! You win!")
            user_score = user_score + 1
        else:
            print("Hunter kills Bear! You lose.")
            computer_score = computer_score + 1

    print(f"User score: {user_score}, Computer score: {computer_score}")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "n":
        break


print(f"Player final tally: {user_score}")
print(f"Computer final score: {computer_score}")
