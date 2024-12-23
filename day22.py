import math

secretNums = []
with open("input/day22.txt", "r") as file:
    for line in file:
        secretNums.append(int(line))

def calc2000ThSecretNum(num):
    currentNum = num
    for _ in range(2000):
        # Multiply by 64, mix, prune
        currentNum = ((currentNum * 64) ^ currentNum) % 16777216

        # Divide by 32, round down, mix, prune
        currentNum = (math.floor(currentNum / 32) ^ currentNum) % 16777216

        # Multiply by 2048, mix, prune
        currentNum = ((currentNum * 2048) ^ currentNum) % 16777216
    
    return currentNum

print("Part 1:", sum(map(calc2000ThSecretNum, secretNums)))