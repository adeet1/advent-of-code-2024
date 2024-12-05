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
