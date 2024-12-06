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

for row in grid:
    print(row)

class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

visited = {}
currentRow = None
currentCol = None
direction = Direction.NORTH
for r in range(len(grid)):
    for c in range(len(grid[r])):
        cell = grid[r][c]

        if cell == '^':
            visited[(r, c)] = True
            currentRow = r
            currentCol = c
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
        print("Turned right, now facing", direction)
    else:
        # mark the current cell as visited
        visited[(currentRow, currentCol)] = True
        print("Just visited", currentRow, currentCol)
    
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

# Number of distinct cells that were visited
print("Part 1:", sum(visited.values()))