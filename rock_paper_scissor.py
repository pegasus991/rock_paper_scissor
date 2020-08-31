import random
comp_wins = 0
player_wins = 0

def choose_option():
    user_choice = input("Choose rock , paper or scissors: ")
    if user_choice in ["Rock","rock"]:
        user_choice = "rock"
    elif user_choice in ["Paper","paper"]:
        user_choice = "paper"
    elif user_choice in ["Scissor","scissor"]:
        user_choice = "scissor"
    else:
        print("I don't understand , Please try again !!")
        choose_option()
    return user_choice

def computer_option():
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "rock"
    elif comp_choice == 2:
        comp_choice = "paper"
    else:
        comp_choice = "scissor"
    return comp_choice

while True:
    print("")
    user_choice = choose_option()
    comp_choice = computer_option()
    print("")

    if user_choice == comp_choice:
        print("It is a tie !!")
    elif user_choice == "rock":
        if comp_choice == "paper":
            print("The computer won !!")
            comp_wins += 1
        elif comp_choice == "scissor":
            print("The player won !!")
            player_wins += 1
    elif user_choice == "paper":
        if comp_choice == "rock":
            print("The player won !!")
            player_wins += 1
        elif comp_choice == "scissor":
            print("The computer won !!")
            comp_wins += 1
    elif user_choice == "scissor":
        if comp_choice == "rock":
            print("The computer won !!")
            comp_wins += 1
        elif comp_choice == "paper":
            print("The player won !!")
            player_wins += 1
    
    print("points of player: {}".format(player_wins))
    print("points of computer: {}".format(comp_wins))

    user_choice = input("\nDo you want to play again ?? (y/n) ")
    if user_choice in ["Y" , "y"]:
        print("That is the spirit !! Lets go !!")
        continue
    elif user_choice in ["N" , "n"]:
        print("Thanks for playing the game !!")
        break
    else:
        break
