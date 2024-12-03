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

# For each report, delete only the first level and check if it's safe, then
# delete only the second level and check if it's safe, etc.
def isSafePart2(report):
    for i in range(len(report)):
        if isSafe(report[0:i] + report[i+1:]):
            return True

    return False

print("Part 2:", np.sum(list(map(isSafePart2, reports))))