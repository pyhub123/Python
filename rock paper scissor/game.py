import random

def rock_paper_scissor():
    options = ["rock", "paper", "scissor"]

    user_wins = 0
    computer_wins = 0
    attempts = 0
    max_attempts = 3  
    
    while(attempts<max_attempts):
        user_input = input("Type rock/paper/scissor or q to quit: ").lower()
        
        if user_input == "q":
            quit(print("Bye-Bye"))
                
        if user_input not in options:
            continue 
        
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")
        
        if user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
                
        elif user_input == "rock" and computer_pick == "scissor":
            print("You won!")
            user_wins += 1
                
        elif user_input == "scissor" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
                
        elif user_input == computer_pick:
            print("It's a draw!")
                
        elif user_input == "paper" and computer_pick == "scissor":
            print("You lost!")
            computer_wins += 1
                
        elif user_input == "rock" and computer_pick == "paper":
            print("You lost!")
            computer_wins += 1   
                
        elif user_input == "scissor" and computer_pick == "rock":
            print("You lost!")
            computer_wins += 1
        
        attempts += 1
        
    user_score = user_wins
    computer_score = computer_wins  

    if user_score > computer_score:
        print("Congrats! You Won The Game!")
            
    elif user_score < computer_score:
        print("You lost the match! Better Luck Next Time.")
            
    elif user_score == computer_score:
        print("What an Intense match! This match is draw")
    
rock_paper_scissor()
