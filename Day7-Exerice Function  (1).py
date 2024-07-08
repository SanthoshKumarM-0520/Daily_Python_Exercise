"""Rock Paper Scissors"""
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

def icon_print(choice):
    if choice == "rock":
        print(rock)
    elif choice == "paper":
        print(paper)    
    elif choice == "scissors":
        print(scissors)

def result(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw.")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    else:
        print("You lose.")

start_input = input("Welcome to the game. Press 'ENTER' to start.\n").lower()

if start_input == "enter":
    condition = "continue"
    
    while condition == "continue":
        elements = ["rock", "paper", "scissors"]
        user_input = input("What is your choice? Rock, Paper, or Scissors? ").lower()
        
        if user_input in elements:
            icon_print(choice=user_input)
        else:
            while user_input not in elements:
                print("Please enter a valid choice.")
                user_input = input("What is your choice? Rock, Paper, or Scissors? ").lower()
            icon_print(choice=user_input)
        
        computer_choice = random.choice(elements)
        print(f"Computer's choice is: {computer_choice}")
        icon_print(choice=computer_choice)
        
        result(user_choice=user_input, computer_choice=computer_choice)
        
        again = input("Do you want to continue or end? ").lower()
        
        if again == "end":
            condition = "end"
            print("Goodbye.")
        elif again == "continue":
            condition = "continue"
        else:
            while again != "end" and again != "continue":
                print("Please choose 'continue' or 'end'.")
                again = input("Do you want to continue or end? ").lower()
else:
    print("Invalid command. Please start again.")

