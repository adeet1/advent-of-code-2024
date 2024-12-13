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

# print all possible trails

trailheadScores = {} # trailhead coordinates -> score

# Scan the entire grid for all trailheads, and populate the scores dictionary
for r in range(len(topMap)):
    for c in range(len(topMap[r])):
        if topMap[r][c] == 0:
            trailheadScores[(r, c)] = 0

print(trailheadScores.keys())

# Checks that a set of coordinates is inside the grid
def inBounds(r, c):
    if r < 0 or r >= len(topMap):
        return False
    if c < 0 or c >= len(topMap[0]):
        return False
    return True

# Count the number of 9s visited from each trailhead
def computeTrailheadScore(r, c, currentScore=0):
    print("computeTrailheadScore({}, {}, {})".format(r, c, currentScore))

    height = topMap[r][c]
    # base case: we found a complete hiking trail
    if height == 9:
        currentScore += 1
        return currentScore

    # look up, down, left, right
    if inBounds(r-1, c):
        print("up from", (r, c))
        if topMap[r-1][c] == 1 + height:
            return computeTrailheadScore(r-1, c, currentScore)

    if inBounds(r+1, c):
        print("down from", (r, c))
        if topMap[r+1][c] == 1 + height:
            return computeTrailheadScore(r+1, c, currentScore)
    
    if inBounds(r, c-1):
        print("left from", (r, c))
        if topMap[r][c-1] == 1 + height:
            return computeTrailheadScore(r, c-1, currentScore)
    
    if inBounds(r, c+1):
        print("right from", (r, c))
        if topMap[r][c+1] == 1 + height:
            return computeTrailheadScore(r, c+1, currentScore)

    return currentScore

# every time we reach a 9, increment the score for the trailhead we started from
trails = {}
for trailhead in trailheadScores.keys():
    r, c = trailhead

    # Array to keep track of which locations are visited
    visited = defaultdict(bool)

    trails[trailhead] = computeTrailheadScore(r, c)
print("")
print(trails)

"""
{(0, 2): [(0, 2), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4)], (0, 4): [(0, 4), (1, 4), (1, 3), (2, 3), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4)], (2, 4): [(2, 4), (1, 4), (1, 3), (2, 3), (3, 3), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4)], (4, 6): [(4, 6), (5, 6), (5, 7), (4, 7), (3, 7), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5)], (5, 2): [(5, 2), (5, 3), (6, 3), (6, 2), (7, 2), (7, 3), (7, 4), (7, 5), (6, 5), (6, 4)], (5, 5): [(5, 5), (5, 6), (5, 7), (4, 7), (3, 7), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5)], (6, 0): [(6, 0), (7, 0)], (6, 6): [(6, 6), (5, 6), (5, 7), (4, 7), (3, 7), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5)], (7, 1): [(7, 1), (6, 1), (5, 1), (5, 0), (4, 0), (4, 1), (3, 1), (2, 1), (1, 1), (0, 1)]}

"""
