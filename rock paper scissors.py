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

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
user_choice=int(input("Please choose 0 for rock, 1 for paper and 2 for scissor \n"))
if user_choice>=0 and user_choice<3:
    print(game_images[user_choice])
computer_choice= random.randint(0,2)
print("Computer choice is:")
print(game_images[computer_choice])
if user_choice >=3 or user_choice<0:
    print("You've made an invalid choice")
elif user_choice == computer_choice:
    print("IT'S A DRAW")
elif computer_choice == 0 and user_choice == 2:
    print("YOU LOSE")
elif computer_choice==2 and user_choice== 0:
    print("YOU WIN")
elif computer_choice > user_choice:
    print("YOU LOSE")
elif user_choice> computer_choice:
    print("YOU WIN")

