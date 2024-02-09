import random

def get_choice():
  player_choice = input("Eneter your choice here(rock , scissors , paper): ")
  options = ["rock","paper","scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice , "computer" : computer_choice}

  return choices

def check_win(player_choice , computer_choice):
  print(f"You chose {player_choice} and computer chose {computer_choice}")
  if(player_choice==computer_choice):
    return "draw"
  elif(player_choice=="rock" and computer_choice=="scissors"):
    return "player"
  elif(player_choice=="paper" and computer_choice=="rock"):
    return "player"
  elif(player_choice == "scissors" and computer_choice=="paper"):
    return "player"
  else:
    return "computer"

def print_result(result):
  if(result=="player"):
    print("You won")
  elif(result=="computer"):
    print("You lost")
  else:
    print("It's a draw")


print("Welcome, you can play the game rock , paper , scissors. Enter 'stop' to quit")

while(True):
  choices = get_choice()
  if(choices["player"] == "rock" or choices["player"] == "scissors" or choices["player"] == "paper"):
    result = check_win(choices["player"] , choices["computer"])
    print_result(result)
  elif(choices["player"] == "stop"):
    print("Exiting the game, thank you for playing")
    break
  else:
    print("invalid choice")
