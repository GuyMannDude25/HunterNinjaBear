
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
    user = input("Hunter, Ninja or Bear): ")
    possible_actions = ["Hunter", "Ninja", "Bear"]
    computer = random.choice(possible_actions)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user.lower() == computer.lower():
        print(f"Both players selected {user}, play again!")
    elif user.lower() == "Hunter":
        if computer.lower() == "Bear":
            print("Hunter kills Bear! You win!")
            user_score = user_score + 1
        else:
            print("Ninja karate chops Hunter! You lose.")
            computer_score = computer_score + 1
    elif user.lower() == "Ninja":
        if computer.lower() == "Hunter":
            print("Ninja karate chops Hunter! You win!")
            user_score = user_score + 1
        else:
            print("Bear mauls Ninja! You lose.")
            computer_score = computer_score + 1
    elif user.lower() == "Bear":
        if computer.lower() == "Ninja":
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
print(f"Computer final tally: {computer_score}")
