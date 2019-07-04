#
# It's a Start!
#
import random


def roll_dice(dx):
	dice_type = {
		"d4": 	4,
		"d6": 	6,
		"d8": 	8,
		"d10": 	10,
		"d12": 	12,
		"d20": 	20,
		"d100": 100
	}

	roll_result = random.randint(1, dice_type[dx])
	return roll_result


while True:
	print("_" * 50)
	control = input("Press enter to roll a d20!\n" "Type quit to exit: ")

	if control == '':
		rollResult = roll_dice('d20')
		print("You've rolled a {}".format(rollResult))
		if rollResult == 20:
			print("It's a critical!")
		elif rollResult == 1:
			print("Oof! Critical failure!")

	if control == "quit":
		break
