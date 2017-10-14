player_1 = input("Player 1 name : ")
player_2 = input("Player 2 name : ")
point_player_1 = 0
point_player_2 = 0 

def compare(p1,p2):
    if p1 == p2 and (p1 == "rock" or p1 == "scissor" or p1 == "paper"):
        print("It's tie!!\nPlease continue")
        return True
    if (p1 == "rock" and p2 == "scissors") or (p1 == "scissors" and p2 == "paper") or (p1 == "paper" and p2 == "rock"):
        print (player_1 + " wins.")
        if input("Do you want to play another game (yes/no) : ") == "yes":
            return True
        else:
            return False
    elif (p2 == "rock" and p1 == "scissors") or (p2 == "scissors" and p1 == "paper") or (p2 == "paper" and p1 == "rock"):
        print (player_2 + " wins.")
        if input("Do you want to play another game (yes/no) : ") == "yes":
            return True
        else:
            return False
    else:
        print("Invalid input\nplz try again!!!")
        return True

check = True
print("plz input (rock/scissors/paper)")
while check:
    check = compare(input(player_1 + " : "),input(player_2 + " : "))

