puzzle = []
with open("input/day4.txt", "r") as file:
    puzzle = [list(line)[:-1] for line in file] # we don't need '\n', so index up to -1

count = 0

def isXmas(word):
    return word == ["X", "M", "A", "S"]

# Count the number of horizontal occurrences of "XMAS" (forwards)
for r in range(len(puzzle)):
    for c in range(0, len(puzzle[r])-3):
        word = [puzzle[r][c+i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of horizontal occurrences of "XMAS" (backwards)
for r in range(len(puzzle)):
    for c in range(3, len(puzzle[r])):
        word = [puzzle[r][c-i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of vertical occurrences (forward)
for r in range(len(puzzle)-3):
    for c in range(len(puzzle[r])):
        word = [puzzle[r+i][c] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of vertical occurrences (backward)
for r in range(3, len(puzzle)):
    for c in range(len(puzzle[r])):
        word = [puzzle[r-i][c] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of down-and-right diagonal occurrences
for r in range(len(puzzle)-3):
    for c in range(len(puzzle[r])-3):
        word = [puzzle[r+i][c+i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of up-and-right diagonal occurrences
for r in range(3, len(puzzle)):
    for c in range(len(puzzle[r])-3):
        word = [puzzle[r-i][c+i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of down-and-left diagonal occurrences
for r in range(len(puzzle)-3):
    for c in range(3, len(puzzle[r])):
        word = [puzzle[r+i][c-i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

# Count the number of up-and-left diagonal occurrences
for r in range(3, len(puzzle)):
    for c in range(3, len(puzzle[r])):
        word = [puzzle[r-i][c-i] for i in range(0, 4)]
        if isXmas(word):
            # print("row", r, "col", c, word)
            count += 1

print("Part 1:", count)

# 2372 is too low (I had this because my loops were in range(len(puzzle)-4) instead of range(len(puzzle)-3)),
# meaning that I wasn't searching the last row/column of the grid
#
# Checking if the word was XMAS or SAMX (instead of just XMAS) made things more confusing to debug - this resulted
# in me double-counting words, e.g. by searching down-right and up-left
#
# 3901 is too high

"""
M.S
.A.
M.S.

M.M
.A.
S.S

S.M
.A.
S.M

S.S
.A.
M.M
"""

# Count the number of X-MAS
def isX_mas(grid):
    diag1 = [grid[i][i] for i in range(0, len(grid))]
    # print(diag1)
    diag2 = [grid[i][i] for i in range(len(grid)-1, -1, -1)]
    # print(diag2)

    return (diag1 == ["M", "A", "S"] or diag1 == ["S", "A", "M"]) and \
    (diag2 == ["M", "A", "S"] or diag2 == ["S", "A", "M"])

count = 0
for r in range(len(puzzle)-2):
    for c in range(len(puzzle[r])-2):
        subgrid = [puzzle[r+i][c:c+3] for i in range(0, 3)]
        if isX_mas(subgrid):
            count += 1
            for row in subgrid:
                print(row, "count=", count)
        else:
            for row in subgrid:
                print(row)
        print("")

    print("------")

print("Part 2:", count)

# 2535 is too high