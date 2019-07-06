#
# It's a Start!
#
# import random
#
#
# def roll_dice(dx):
# 	dice_type = {
# 		"d4": 	4,
# 		"d6": 	6,
# 		"d8": 	8,
# 		"d10": 	10,
# 		"d12": 	12,
# 		"d20": 	20,
# 		"d100": 100
# 	}
#
# 	roll_result = random.randint(1, dice_type[dx])
# 	return roll_result
#
#
# while True:
# 	print("_" * 50)
# 	control = input("Press enter to roll a d20!\n" "Type quit to exit: ")
#
# 	if control == '':
# 		rollResult = roll_dice('d20')
# 		print("You've rolled a {}".format(rollResult))
# 		if rollResult == 20:
# 			print("It's a critical!")
# 		elif rollResult == 1:
# 			print("Oof! Critical failure!")
#
# 	if control == "quit":
# 		break

import random
import enum

die_sides = {
	"d4": 	4,
	"d6": 	6,
	"d8": 	8,
	"d10": 	10,
	"d12": 	12,
	"d20": 	20,
	"d100": 100
}


class DieType(enum.IntEnum):
	d4 = 4
	d6 = 6
	d8 = 8
	d10 = 10
	d12 = 12
	d20 = 20
	d100 = 100


class Die:
	def __init__(self: None,
				 die_type: str):
		self.die_type = die_type

	def get_die_type(self):
		return self.die_type

	def roll_die(self: None):
		return random.randint(1, die_sides[self.die_type])

	def average(self: None):
		return (die_sides[self.die_type] + 1) / 2


class TestRoll:
	def __init__(self,
				 mod_value: int,
				 adv=False,
				 dis=False,
				 half=False,
				 lucky=False):
		self.mod_value = mod_value
		self.adv = adv
		self.dis = dis
		self.half = half
		self.lucky = lucky

		self.dice_bundle = [Die("d20")]

	# def change(self,
	# 		   adv=,
	# 		   dis=dis,
	# 		   half=False,
	# 		   lucky=False,
	# 		   ):
	# 	self.adv = adv
	# 	self.

	def status(self):
		print("Modifier Value: \t{}".format(self.mod_value))
		print("Has Advantage: \t\t{}".format(self.adv))
		print("Has Disadvantage: \t{}".format(self.dis))
		print("Use Luck Point: \t{}".format(self.lucky))
		print("Is Halfling: \t\t{}".format(self.half))
		print("-" * 40)

	def add_die(self,
				sides: str):
		self.dice_bundle.append(Die(sides))

	def get_dice_bundle(self):
		return self.dice_bundle

	def resolve(self):

		d20_roll = Die('d20').roll_die()
		return d20_roll + self.mod_value
