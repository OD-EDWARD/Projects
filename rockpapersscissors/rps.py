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
---'    ____)____
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
user_choice = input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors?")

computer_choice = random.randint(0,2)
print(f"computer_choice{computer_choice}")
