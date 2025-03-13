from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
prs = ["rock", "paper", "scissors"]
computer = prs[num-1]

# Ask a user to enter their move
move = input("Enter your move: rock, paper, or scissors: ")

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if move == "rock":
    print(rock)
elif move == "paper":
    print(paper)
elif move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(f"""
      Computer chose: {computer}""")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)

# Figure out who wins and print the result!
if move == computer:
    print("It's a tie!")
elif move == "rock" and computer == "scissors":
    print("You win!")
elif move == "paper" and computer == "rock":
    print("You win!")
elif move == "scissors" and computer == "paper":
    print("You win!")
else:
    print("you lose!")