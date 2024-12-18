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

# Checks that a set of coordinates is inside the grid
def inBounds(r, c):
    if r < 0 or r >= len(topMap):
        return False
    if c < 0 or c >= len(topMap[0]):
        return False
    return True

# Count the number of 9s visited from each trailhead
def computeTrailheadScore(r, c, nines=set()):
    height = topMap[r][c]

    # base case: we found a stop
    if height == 9:
        nines.add((r, c))
        return

    # look up, down, left, right
    if inBounds(r-1, c):
        if topMap[r-1][c] == 1 + height:
            computeTrailheadScore(r-1, c, nines)

    if inBounds(r+1, c):
        if topMap[r+1][c] == 1 + height:
            computeTrailheadScore(r+1, c, nines)
    
    if inBounds(r, c-1):
        if topMap[r][c-1] == 1 + height:
            computeTrailheadScore(r, c-1, nines)
    
    if inBounds(r, c+1):
        if topMap[r][c+1] == 1 + height:
            computeTrailheadScore(r, c+1, nines)

trailheadScores = {} # trailhead coordinates -> score
for r in range(len(topMap)):
    for c in range(len(topMap[r])):
        if topMap[r][c] == 0:
            trailheadScores[(r, c)] = 0

trails = {}
for trailhead in trailheadScores.keys():
    r, c = trailhead

    stops = set()
    computeTrailheadScore(r, c, stops)
    trails[trailhead] = len(stops)

print("Part 1:", sum(trails.values()))

"""
The number of trails that begin at (r, c) is the sum
of the number of trails that begin from the top, bottom,
left, and right of that location.

Ex: there are 4 trails beginning from the 8.
  9
9 8 9
  9
"""
def computeTrailRating(r, c):
    height = topMap[r][c]
    if height == 9:
        return 1

    score = 0

    # up
    if inBounds(r-1, c):
        if topMap[r-1][c] == 1 + height:
            score += computeTrailRating(r-1, c)
    
    # down
    if inBounds(r+1, c):
        if topMap[r+1][c] == 1 + height:
            score += computeTrailRating(r+1, c)
    
    # left
    if inBounds(r, c-1):
        if topMap[r][c-1] == 1 + height:
            score += computeTrailRating(r, c-1)
    
    # right
    if inBounds(r, c+1):
        if topMap[r][c+1] == 1 + height:
            score += computeTrailRating(r, c+1)
    
    return score

trailRatings = {}
for trailhead in trailheadScores.keys():
    r, c = trailhead
    trailRatings[trailhead] = computeTrailRating(r, c)

print("Part 2:", sum(trailRatings.values()))