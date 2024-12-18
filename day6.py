from enum import Enum
from collections import defaultdict
import copy

grid = []
with open("input/day6.txt", "r") as file:
    for line in file:
        if line == "\n":
            break
        
        row = list(line)
        if row[-1] == "\n":
            grid.append(row[:-1])
        else:
            grid.append(row)

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

def guardWalk(grid):
    visitedCells = {}
    currentRow = None
    currentCol = None
    direction = Direction.NORTH
    visitedHeadStates = defaultdict(bool)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell = grid[r][c]

            if cell == '^':
                visitedCells[(r, c)] = True
                currentRow = r
                currentCol = c
            elif cell == '.':
                visitedCells[(r, c)] = False
            else:
                # do not add obstacle cells ('#') to visitedCells, since it's impossible to visit them
                # and we need a way to distinguish between obstacle and non-obstacle cells
                pass

    def turnRight():
        match direction:
            case Direction.NORTH:
                return Direction.EAST
            case Direction.EAST:
                return Direction.SOUTH
            case Direction.SOUTH:
                return Direction.WEST
            case Direction.WEST:
                return Direction.NORTH

    cycleExists = False
    # Start walking up, keep walking until we hit an obstacle
    while currentRow >= 0 and currentRow < len(grid) and currentCol >= 0 and currentCol < len(grid[currentRow]):
        if grid[currentRow][currentCol] == '#':
            # Move out of the obstacle
            match direction:
                case Direction.NORTH:
                    currentRow += 1
                case Direction.EAST:
                    currentCol -= 1
                case Direction.SOUTH:
                    currentRow -= 1
                case Direction.WEST:
                    currentCol += 1

            direction = turnRight()
        else:
            # mark the current cell as visited
            visitedCells[(currentRow, currentCol)] = True
            
            # if we've already been at this cell, facing in the same direction
            # as we were when previously at this cell, it means we'll be stuck
            # in a loop
            if visitedHeadStates[((currentRow, currentCol), direction.name)]:
                cycleExists = True
                break
            
            visitedHeadStates[((currentRow, currentCol), direction.name)] = True
        
        # move in the correct direction
        match direction:
            case Direction.NORTH:
                currentRow -= 1
            case Direction.EAST:
                currentCol += 1
            case Direction.SOUTH:
                currentRow += 1
            case Direction.WEST:
                currentCol -= 1
    
    return sum(visitedCells.values()), visitedHeadStates, cycleExists

# Number of distinct cells that were visited
numCells, visitedHeadStates, _ = guardWalk(grid)
print("Part 1:", numCells)

# Part 2 ===================

# Place an obstacle along each cell the guard has visited (except its starting position),
# and see if the guard gets stuck in a loop.

numObstaclePositions = set()
for newObstacle, _ in visitedHeadStates:
    r, c = newObstacle

    tmpGrid = copy.deepcopy(grid)
    if tmpGrid[r][c] == '^': # can't place an obstacle at the guard's starting position
        continue

    # Place the obstacle and simulate the guard walking around
    tmpGrid[r][c] = '#'
    _, path, cycleExists = guardWalk(tmpGrid)
    if cycleExists:
        tmpGrid[r][c] = 'O' # for debugging, in case we want to print the grid
        numObstaclePositions.add(newObstacle)

print("Part 2:", len(numObstaclePositions))