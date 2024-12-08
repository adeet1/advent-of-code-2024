from enum import Enum

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
    visited = {}
    currentRow = None
    currentCol = None
    direction = Direction.NORTH
    guardPath = []
    isFirstCell = True
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            cell = grid[r][c]

            if cell == '^':
                visited[(r, c)] = True
                currentRow = r
                currentCol = c
                guardPath.append(((r, c), direction.name))
            elif cell == '.':
                visited[(r, c)] = False
            else:
                # do not add obstacle cells ('#') to visited, since it's impossible to visit them
                # and we need a way to distinguish between obstacle and non-obstacle cells
                pass

    # Start walking up, keep walking until we hit an obstacle

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
            visited[(currentRow, currentCol)] = True
            
            # if we've already been at this cell, facing in the same direction
            # as we were when previously at this cell, it means we'll be stuck
            # in a loop
            if ((currentRow, currentCol), direction.name) in guardPath:
                cycleExists = True
            
            guardPath.append(((currentRow, currentCol), direction.name))
        
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
        
        isFirstCell = False
    
    return sum(visited.values()), guardPath, cycleExists

# Number of distinct cells that were visited
numCells, guardPath, cycleExists = guardWalk(grid)
print("Part 1:", numCells)
#print(guardPath)
print(cycleExists)


# Part 2 ===================

# Put an obstacle along every cell the guard has visited (except its starting position),
# and see if the guard gets stuck in a loop (i.e. if it's already visited a cell and is
# facing in the same direction)

for newObstacle, _ in guardPath[1:]: # don't put obstacle at its starting position
    r, c = newObstacle
    grid[r][c] = '#'




# To figure out if the guard is stuck in a loop or not, I could
# just run the above code and see if the number of distinct visited
# cells stays the same despite the guard moving. and if it does, it
# means he's stuck in a loop.
#
# Original brute force idea: put an obstacle at every cell and rerun
# the above code to see where loops happen. But this is too slow because
# there's no point in placing obstacles at cells the guard never reaches.
# Instead, we want to filter down only to cells that the guard visits (the
# list guardPath).