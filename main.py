import random

def get_choices():#Functions Get_Choice
    print('-------------------------------------------------------')
    print('Welcome to the game player with a computer')
    print('---------------------------------------------------------')
    player_choice=input("Enter a choice [rock,paper,scissors:] ") # Player_choice is the variable & we assign string Rock to the variable
    option=["rock", "paper", "scissors"]
    computer_choice=random.choice(option)
    choices = {"player" :player_choice,"computer" :computer_choice}
    return choices

def check_win(player,computer):

    print(f"You chose :{player}, computer chose :{computer}")

    if player==computer:

     return "Its a tie!"
    
    elif player=="rock":
       
       if computer=="scissors":
          
          return"Rocks Smashes Scissors! You win!"
       
       else:
          
          return"Paper Covers rocks! You lose" 
       
    elif player=="paper":
       
       if computer=="rock":
          
          return "Paper Covers rocks! You win"
       
       else:
          
          return"Scissors cuts paper!You lose."
       
    elif player=="Scissors":
       if computer=="Paper":
          return"Scissors Cuts paper!You win"
       else:
          return"Rocks smashes scissors! You lose"
       
choices=get_choices()
result=check_win(choices ["player"], choices ["computer"])
print(result)

