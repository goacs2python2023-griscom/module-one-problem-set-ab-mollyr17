import random

def roll_dice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    total = x + y
    print (x)
    print(y)
    if total >= 6 and total <= 8:
        return "win"
    else:
        return "lose"

print (roll_dice())