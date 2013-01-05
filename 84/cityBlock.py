from itertools import permutations
import sys

points = []

for p in sys.stdin.readlines():
	points.append((int(p.split()[0]), int(p.split()[1])))

print points

distances = [[abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) for i in range(len(points))] for j in range(len(points))]

max_steps = []
max_dist = None

min_steps = []
min_dist = None

for steps in permutations(range(len(points)), len(points)):
	dist = 0
	for step in range(len(steps) - 1):
		dist += distances[steps[step]][steps[step+1]]

	if max_dist is None or dist > max_dist:
		max_dist = dist
		max_steps = steps

	if min_dist is None or dist < min_dist:
		min_dist = dist
		min_steps = steps

print "Minimum distance: %d" % min_dist
print min_steps
print "Maximum distance: %d" % max_dist
print max_steps