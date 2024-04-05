import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

game_list = ["rock", "paper", "scissors"]
 
computer_choice = random.choice([0,1,2])

user_choice = int(user_input)

if user_choice == 0 and computer_choice == 2:
  print(f"{rock}\n Cimputer chose: \n {scissors} \n You won!!")
elif user_choice == 0 and computer_choice == 0:
  print(f"{rock}\n Cimputer chose: \n {rock} \n try again!!")
elif user_choice == 0 and computer_choice == 1:
  print(f"{rock}\n Cimputer chose: \n {paper} \n You lose!!")

if user_choice == 1 and computer_choice == 0:
  print(f"{paper}\n Cimputer chose: \n {rock} \n You won!!")
elif user_choice == 1 and computer_choice == 1:
  print(f"{paper}\n Cimputer chose: \n {paper} \n try again!!")
elif user_choice == 1 and computer_choice == 2:
  print(f"{paper}\n Cimputer chose: \n {scissors} \n You lose!!")

if user_choice == 2 and computer_choice == 1:
  print(f"{scissors}\n Cimputer chose: \n {paper} \n You won!!")
elif user_choice == 2 and computer_choice == 2:
  print(f"{scissors}\n Cimputer chose: \n {scissors} \n try again!!")
elif user_choice == 2 and computer_choice == 0:
  print(f"{scissors}\n Cimputer chose: \n {rock} \n You lose!!")