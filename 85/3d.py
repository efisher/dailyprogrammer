import sys

topChar = ":"
frontChar = "#"
sideChar = "+"
spaceChar = " "
cornerChar = "/"

if len(sys.argv) != 4:
	print "Usage: 3d.py l h d"
	quit()
else:
	length = int(sys.argv[1])
	height = int(sys.argv[2])
	depth = int(sys.argv[3])

for i in range(depth + height):
	if i < depth:
		print spaceChar * (depth - i) + topChar * length + cornerChar + sideChar * i
	elif i < height:
		print frontChar * length + sideChar * depth
	else:
		print frontChar * length + sideChar * (depth + height - i - 1)