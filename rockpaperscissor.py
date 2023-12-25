import random

comp_wins = 0
player_wins = 0

def Choose_Option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock" , "rock" ,"r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice

def Computer_Option():
    comp_choice = random.randint (1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice  

while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")
    
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You Tied.")
        elif comp_choice == "p":
            print("You chose rock. The computer chose paper. You Lose.")
            comp_wins += 1
            
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You Won!")
            player_wins += 1
            
    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You Won!")
            player_wins += 1
            
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You Tied.")
            
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You Lose.")
            comp_wins += 1
            
    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You Lose.")
            comp_wins += 1
            
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You Won!")
            player_wins += 1
            
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You Tied.")
            
    print("")
    print("Player Wins: " + str(player_wins))
    print("Computer Wins: " + str(comp_wins))
    print("")
    
    user_choice = input("Play Again? (y/n) ")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
                                                                               
        
