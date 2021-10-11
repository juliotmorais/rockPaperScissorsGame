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

print("Welcome to Rock Paper Scissors!")
choice = input("For Rock, enter '0', for Paper, enter '1', for Scissors, enter '2': ")

opponent= random.randint(0,2)

print("Your sign: ")
if choice =="0":
    print(rock)
elif choice =="1":
    print(paper)
elif choice =="2":
    print(scissors)

print("Your opponents sign: ")
if opponent ==0:
    print(rock)
elif opponent ==1:
    print(paper)
elif opponent ==2:
    print(scissors)

if (choice =="0" and opponent == 0) or (choice =="1" and opponent == 1) or (choice =="2" and opponent ==2 ):
    print("TIE!")
elif((choice=="0" and opponent == 2) or (choice=="1" and opponent == 0) or (choice=="2" and opponent == 0)):
    print("WIN!")
else:
    print("YOU LOSE!")
