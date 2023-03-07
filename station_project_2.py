import random


def dice_sum():
    first = random.randint(1, 6)
    second = random.randint(1, 6)
    print(f"The sum of dice is {first} + {second} = {first + second}")
    return first + second


input("Press enter to start")
result = dice_sum()
if result == 7 or result == 11:
    print("You won")
elif result == 2 or result == 3 or result == 12:
    print("You lose")
else:
    print(f"Now your goal number is {result}")
    goal_number = result
    while result != 7:
        result = dice_sum()
        if result == goal_number:
            print("You won")
            break
    else:
        print("You lose")

