import random


def get_choice():
    player_choice = input("Enter Choice: [r]ock, [p]aper, or [s]cissors")
    option = ["rock", "paper", "scissors"]
    com_choice = random.choice(option)
    choices = {"Player": player_choice, "computer": com_choice}
    return choices

def check_win(player, com):
    print("You chose " + player + " Computer chose " + com)
    if player == com:
        return "It's a tie"
    elif player == "rock":
        if com == "paper":
            return "Computer wins"
        else:
            return "You win"
    elif player == "scissors":
        if com == "rock":
            return "Computer wins"
        else:
            return "You win"
    elif player == "paper":
        if com == "scissors":
            return "Computer wins"
        else:
            return "You win" 

choices = get_choice()
result = check_win(choices["Player"], choices["computer"])
print(result)