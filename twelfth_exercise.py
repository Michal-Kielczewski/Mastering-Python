player1 = input("Please enter player 1 your name: ")
player2 = input("Please enter player 2 your name: ")

num = 13
tooth = "| "

while num > 0:
    print(tooth * num)
    print(f"There are {num} toothpicks left")
    player1_take= int(input(f"How many do you take, {player1}?"))
    while player1_take not in range(1, 4):
        player1_take = int(input("You can only take 1, 2, or 3: "))
    num -= player1_take
    if num <= 0:
        print(f"{player1} wins the game!")
        break

    print(tooth* num)
    print(f"There are {num} toothpicks left")
    player2_take= int(input(f"How many do you take, {player2}?"))
    while player2_take not in range(1, 4):
        player2_take = int(input("You can only take 1, 2, or 3: "))
    num -= player2_take
    if num <= 0:
        print(f"{player2} wins the game!")
        break

print("GAME OVER!")
