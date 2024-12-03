import numpy as np

left = []
right = []

# Open the file and create the two lists
with open("input/day1.txt", "r") as file:
    for line in file:
        a, b = [int(x) for x in line.split("   ")]
        left.append(a)
        right.append(b)

# Pair up the smallest number on the left with the smallest on the right, etc.
# by sorting them
left = np.sort(left)
right = np.sort(right)

# Compute the total distance of the lists
print(np.sum(np.abs(left - right)))