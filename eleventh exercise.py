from random import randint

dice_num = 0
while dice_num not in range(1, 21):
    dice_num = input("Please enter the number of dice you'd like to roll from 1 to 20: ")
    if dice_num.isdigit():
        dice_num = int(dice_num)
        if dice_num not in range(1, 21):
            print("Number out of range. Please try again.")
            dice_num = 0
    else:
        print("Please enter a valid number.")
        dice_num = 0

dice_sides = 0
while dice_sides not in range(4, 21):
    dice_sides = input("Please enter the number of sides on each die form 4 to 20: ")
    if dice_sides.isdigit():
        dice_sides = int(dice_sides)
        if dice_sides not in range(4, 21):
            print("Number out of range. Please try again.")
            dice_sides = 0
    else:
        print("Please enter a valid number.")
        dice_sides = 0
    dice_sides = int(dice_sides)


one_more_time = ""
while one_more_time != "q":
    final_result = []
    for i in range(dice_num):
        result = (randint(1, dice_sides))
        final_result.append(result)
    print(final_result)
    one_more_time = input("Roll again? ('q') to quit: ")
    
