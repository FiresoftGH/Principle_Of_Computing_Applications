import sys
valid_input = ["rock","paper","scissors"]
def space():
    for x in range(20):
        print(" ")
while True:
    try:
        player_1 = str(input("Rock, Paper or Scissors?: ").lower())
        space()
        player_2 = str(input("Rock, Paper or Scissors?: ").lower())
        space()
        if player_1 or player_2 not in valid_input:
            print("Invalid input")
            player_1 = str(input("Rock, Paper or Scissors?: "))
            space()
        if player_1 == "rock" and player_2 == "scissors":
            print("Player 1 wins")
        if player_1 == "scissors" and player_2 == "rock":
            print("Player 2 wins")
        if player_1 == "rock" and player_2 == "paper":
            print("Player 2 wins")
        if player_1 == "paper" and player_2 == "rock":
            print("Player 1 wins")
        if player_1 == "scissors" and player_2 == "paper":
            print("Player 1 wins")
        if player_1 == "paper" and player_2 == "scissors":
            print("Player 2 wins")
        if player_1 == player_2:
            print("Tied")
    except KeyboardInterrupt:
        sys.exit(0)
