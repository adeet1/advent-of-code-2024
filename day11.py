initStones = []
with open("input/day11.txt", "r") as file:
    for line in file:
        initStones = [int(x) for x in line.split()]

def blink(stones):
    newStones = []

    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0: # if the stone's number has an even number of digits
            midIndex = len(str(stone)) // 2
            leftStone = int(str(stone)[0:midIndex])
            rightStone = int(str(stone)[midIndex:])
            newStones.append(leftStone)
            newStones.append(rightStone)
        else:
            newStones.append(stone * 2024)
    
    return newStones

stones = initStones
for i in range(25):
    stones = blink(stones)
print("Part 1:", len(stones))