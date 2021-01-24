import sys
from random import randint

def rps():
    if not len(sys.argv) >= 2:
        print("Please give me a sign to play against!")
        exit()

    handsigns = ["Rock", "Paper", "Scissors"]
    losing_states = [("Rock", "Paper"), ("Paper", "Scissors"), ("Scissors", "Rock")]
    player_sign = sys.argv[1].title() # Convert CLI input to work with expected pattern

    # Validate input
    if player_sign not in handsigns:
        print("That isn't a valid sign, smartass!")
        exit()

    comp_sign = handsigns[randint(0,2)]
    if player_sign == comp_sign:
        print("You tied, try again")
        exit()
        
    game_state = (player_sign, comp_sign)
    if game_state in losing_states:
        print("YOU LOSE, SUCKER!")
        exit()
        
    # At this point, we know that user didn't tie or lose to the computer, meaning they must have won
    print("Damn, you beat me.")

if __name__ == "__main__":
    rps()