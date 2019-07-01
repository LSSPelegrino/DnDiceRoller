#
# It's a Start!
#
import random

while True:
	print("_" * 50)
	control = input("Press enter to roll a d20!\n" "Type quit to exit: ")

	if control == '':
		roll = random.randint(1, 20)
		print("You've rolled a {}".format(roll))
		if roll == 20:
			print("It's a critical!")
		elif roll == 1:
			print("Oof! Critical failure!")

	if control == "quit":
		break
