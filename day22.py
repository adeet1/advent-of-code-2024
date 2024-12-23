import math
import numpy as np
from collections import defaultdict

secretNums = []
with open("input/day22.txt", "r") as file:
    for line in file:
        secretNums.append(int(line))

def calcSecretNum(num):
    currentNum = num

    # Multiply by 64, mix, prune
    currentNum = ((currentNum * 64) ^ currentNum) % 16777216

    # Divide by 32, round down, mix, prune
    currentNum = (math.floor(currentNum / 32) ^ currentNum) % 16777216

    # Multiply by 2048, mix, prune
    currentNum = ((currentNum * 2048) ^ currentNum) % 16777216
    
    return currentNum

def calc2000ThSecretNum(num):
    currentNum = num
    for _ in range(2000):
        currentNum = calcSecretNum(currentNum)
    
    return currentNum

print("Part 1:", sum(map(calc2000ThSecretNum, secretNums)))

def calcPricesForBuyer(num):
    prices = np.empty(2000)
    prices[0] = int(str(num)[-1])
    secretNum = num
    for i in range(1, len(prices)):
        secretNum = calcSecretNum(secretNum)

        # Get the ones digit of the current secret number
        prices[i] = int(str(secretNum)[-1])

    return prices

bananas = defaultdict(int)
for buyerNum in secretNums:
    buyerPrices = calcPricesForBuyer(buyerNum)
    diff = np.diff(buyerPrices).astype(int)

    sequenceSeen = defaultdict(bool)

    # Calculate the number of bananas we can get for this buyer, from all sequences of 4 prices
    for i in range(0, len(diff)-4):
        sequence = tuple(diff[i:i+4])
        if sequenceSeen[sequence]:
            continue

        sequenceSeen[sequence] = True
        numBananas = int(buyerPrices[i+4])

        # If we haven't sold bananas yet
        bananas[sequence] += numBananas

print("Part 2:", max(bananas.values()))