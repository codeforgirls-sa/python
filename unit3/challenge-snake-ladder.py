
from random import randint

dice = 0
position = 0
turn = 0

while position < 100:
	dice = randint(1, 6)
	position = position + dice
	turn += 1

	if position == 4:
		position = 14
		print("Yay! a ladder")

	elif position == 9:
		position = 31
		print("Yay! a ladder")

	elif position == 17:
		position = 7
		print("Oh no! a snake")

	elif position == 20:
		position = 38
		print("Yay! a ladder")

	elif position == 28:
		position = 84
		print("Yay! a ladder")

	elif position == 40:
		position = 59
		print("Yay! a ladder")

	print("dice roll is", dice)
	print("player moved to slot " + str(position))

print("player won after " + str(turn) + " turns")