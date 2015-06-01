#!/usr/bin/python
import random
import sys
import re

debugging = False

if len(sys.argv) == 1:
    print("please supply dice to roll ex: 1d6 2d20")
    sys.exit()

dice_to_roll = sys.argv[1]
dnd_dice_check = re.compile('^[0-9]d(4|6|8|10|12|20)$')
if not dnd_dice_check.match(dice_to_roll):
    print("You did not enter a correct D&D dice roll:")
    print("syntax: [number of rolls]d[dice]")
    print("where dice is 4,6,8,10,12 or 20")
    print("examples: 1d6, 2d20, 4d10, etc")

rolls,dice = dice_to_roll.split('d')
rolls = int(rolls)
dice = int(dice)
print("\nRolling " + dice_to_roll + "\n")

if debugging:
    print("rolls %d" % rolls)
    print("dice %d" % dice)

roll_total = 0

for roll in range(0, rolls, 1):

    current_roll = random.randint(1,dice)
    roll_total += current_roll
    print("Roll #%d is %d" % (roll+1,current_roll))

print("Total for roll is: %d" % roll_total)


