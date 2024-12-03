import numpy as np

reports = []
with open("input/day2.txt", "r") as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

def isSafe(report):
    # Compute the deltas (change between adjacent levels)
    deltas = np.diff(report)

    # If the levels are not all increasing or all decreasing, then it's unsafe
    if not (np.all(deltas > 0) or np.all(deltas < 0)):
        return False
    
    # If any two adjacent levels differ by less than 1 or more than 3, then it's unsafe
    if np.any(np.abs(deltas) < 1) or np.any(np.abs(deltas) > 3):
        return False

    return True

print("Part 1:", np.sum(list(map(isSafe, reports))))