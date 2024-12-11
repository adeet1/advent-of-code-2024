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

# Array to keep track of which locations are visited
visited = defaultdict(bool)

trailheadScores = {} # trailhead coordinates -> score

# Scan the entire grid for all trailheads, and populate the scores dictionary
for r in range(len(topMap)):
    for c in range(len(topMap[r])):
        if topMap[r][c] == 0:
            trailheadScores[(r, c)] = 0
            visited[(r, c)] = True # we've already visited trailheads

print(trailheadScores.keys())

# Checks that a set of coordinates is inside the grid
def inBounds(r, c):
    if r < 0 or r >= len(topMap):
        return False
    if c < 0 or c >= len(topMap[0]):
        return False
    return True

# run DFS at each trailhead
def DFS(r, c, trailSoFar=[0]):
    print("DFS({}, {}, {})".format(r, c, trailSoFar))
    
    if not inBounds(r, c):
        return trailSoFar
    
    visited[(r, c)] = True

    height = topMap[r][c]
    # base case: we found a complete hiking trail
    if height == 9:
        return trailSoFar

    # look up, down, left, right
    if inBounds(r-1, c):
        print("up from", (r, c))
        if not visited[(r-1, c)] and topMap[r-1][c] == 1 + height:
            return DFS(r-1, c, trailSoFar + [topMap[r-1][c]])

    if inBounds(r+1, c):
        print("down from", (r, c))
        if not visited[(r+1, c)] and topMap[r+1][c] == 1 + height:
            return DFS(r+1, c, trailSoFar + [topMap[r+1][c]])
    
    if inBounds(r, c-1):
        print("left from", (r, c))
        if not visited[(r, c-1)] and topMap[r][c-1] == 1 + height:
            return DFS(r, c-1, trailSoFar + [topMap[r][c-1]])
    
    if inBounds(r, c+1):
        print("right from", (r, c))
        if not visited[(r, c+1)] and topMap[r][c+1] == 1 + height:
            return DFS(r, c+1, trailSoFar + [topMap[r][c+1]])

    return trailSoFar

# every time we reach a 9, increment the score for the trailhead we started from
trails = {}
for trailhead in trailheadScores.keys():
    r, c = trailhead
    trails[trailhead] = DFS(r, c)
    
print(trails)

"""
1 2 1
0 1 2
1 0 2
"""
