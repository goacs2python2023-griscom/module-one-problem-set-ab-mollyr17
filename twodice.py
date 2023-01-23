import random

#rolls two dice using random package, returns win if sum = 6, 7, or 8, returns lose otherwise
def roll_dice():
    die_one = random.randint(1,6)
    die_two = random.randint(1,6)
    total = die_one + die_two
    print(die_one)
    print(die_two)
    if total >= 6 and total <= 8:
        return "win"
    else:
        return "lose"

print (roll_dice())