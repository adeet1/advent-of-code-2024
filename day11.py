from collections import Counter

initStones = []
with open("input/day11.txt", "r") as file:
    for line in file:
        initStones = [int(x) for x in line.split()]

def changeStone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0: # if the stone's number has an even number of digits
        midIndex = len(str(stone)) // 2
        leftStone = int(str(stone)[0:midIndex])
        rightStone = int(str(stone)[midIndex:])
        return [leftStone, rightStone]
    else:
        return [stone * 2024]

def blink(stoneCounts):
    newStoneCounts = Counter()

    # Look at the current stones
    for (stone, count) in stoneCounts.items():
        # Change this stone's value or split it in two, depending on its value
        newStones = changeStone(stone)

        # Look at each new stone created from this current stone, and update their counts
        for newStone in newStones:
            # There were *count* occurrences of this stone, and we had to change each of them
            newStoneCounts[newStone] += count
    
    return newStoneCounts

# Any stones with the same value will change in the exact same way, so we only
# need to compute the change once and keep track of the number of times each
# stone appears (thus we can memoize things).
#
# We can do so using a counter.
stoneCounts = Counter(initStones)
for i in range(25):
    stoneCounts = blink(stoneCounts)
print("Part 1:", sum(stoneCounts.values()))

stoneCounts = Counter(initStones)
for i in range(75):
    stoneCounts = blink(stoneCounts)
print("Part 2:", sum(stoneCounts.values()))
