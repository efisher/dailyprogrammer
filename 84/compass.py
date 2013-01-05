import random
import math

treasure_loc = [random.randint(-10, 10), random.randint(-10, 10)]

player_loc = [0, 0]

while player_loc != treasure_loc:
	print "The dial reads '%1.3fm'" % math.sqrt(math.pow(treasure_loc[0] - player_loc[0], 2) + math.pow(treasure_loc[1] - player_loc[1], 2))
	direction = raw_input("Which direction will you go?\n")
	if direction == "n":
		player_loc[1] += 1
	elif direction == "e":
		player_loc[0] += 1
	elif direction == "s":
		player_loc[1] -= 1
	elif direction == "w":
		player_loc[0] -= 1
	else:
		print "Please type n, e, s, or w"


print "You found it!"