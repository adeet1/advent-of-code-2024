import numpy as np
from collections import defaultdict

topMap = []
with open("input/day10.txt", "r") as file:
    for line in file:
        row = list(line)
        if row[-1] == "\n":
            row = row[:-1]

        topMap.append([int(x) for x in row])

topMap = np.array(topMap)
print(topMap)

# Checks that a set of coordinates is inside the grid
def inBounds(r, c):
    if r < 0 or r >= len(topMap):
        return False
    if c < 0 or c >= len(topMap[0]):
        return False
    return True

# Count the number of 9s visited from each trailhead
def computeTrailheadScore(r, c, nines=set()):
    print("computeTrailheadScore({}, {})".format(r, c))

    height = topMap[r][c]
    # base case: we found a stop
    if height == 9:
        nines.add((r, c))
        return

    # look up, down, left, right
    if inBounds(r-1, c):
        print("up from", (r, c))
        if topMap[r-1][c] == 1 + height:
            computeTrailheadScore(r-1, c, nines)

    if inBounds(r+1, c):
        print("down from", (r, c))
        if topMap[r+1][c] == 1 + height:
            computeTrailheadScore(r+1, c, nines)
    
    if inBounds(r, c-1):
        print("left from", (r, c))
        if topMap[r][c-1] == 1 + height:
            computeTrailheadScore(r, c-1, nines)
    
    if inBounds(r, c+1):
        print("right from", (r, c))
        if topMap[r][c+1] == 1 + height:
            computeTrailheadScore(r, c+1, nines)

trailheadScores = {} # trailhead coordinates -> score
for r in range(len(topMap)):
    for c in range(len(topMap[r])):
        if topMap[r][c] == 0:
            trailheadScores[(r, c)] = 0

print(trailheadScores.keys())

trails = {}
for trailhead in trailheadScores.keys():
    r, c = trailhead

    stops = set()
    computeTrailheadScore(r, c, stops)
    trails[trailhead] = len(stops)

print("Part 1:", sum(trails.values()))
