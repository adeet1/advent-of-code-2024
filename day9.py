import copy
from collections import Counter

disk = ""
with open("input/day9.txt", "r") as file:
    for line in file:
        disk = [int(_) for _ in list(line)]

def createDiskMap(inputDisk):
    fileId = 0
    diskMap = []

    # Increment the fileId every two elements we iterate through inputDisk
    for i in range(len(inputDisk)):
        # If i is even, then inputDisk[i] represents the number of blocks in the file
        if i % 2 == 0:
            numBlocks = inputDisk[i]
            diskMap += [fileId for _ in range(numBlocks)]
            fileId += 1

        # If i is odd, then inputDisk[i] represents the amount of free space after the file
        if i % 2 == 1:
            numFreeSpaces = inputDisk[i]
            diskMap += [None for _ in range(numFreeSpaces)]
    
    return diskMap

def compactDiskPart1(diskMap):
    # A list containing the indices of diskMap corresponding to free space
    isFreeSpace = [diskMap[_] == None for _ in range(len(diskMap))]
    currentDiskMap = copy.deepcopy(diskMap)
    index = 0
    while index < len(currentDiskMap):
        # print("index =", index, ": file block =", currentDiskMap[index], ": is free space =", isFreeSpace[index])
        if isFreeSpace[index]:
            # Get the last file block
            lastFileBlock = currentDiskMap.pop()
            # print("last file block =", lastFileBlock)

            # Copy that block (only if there's a file there) to the current free space
            # There's no need to copy that block if it's a free space
            if lastFileBlock != None:
                currentDiskMap[index] = lastFileBlock

                # Mark this space as allocated (not free)
                isFreeSpace[index] = False
        
        # We only move to the next index if this space is allocated
        # If this space is free, then stay so we can allocate it later
        else:
            index += 1
        # print("Current disk map:", currentDiskMap[index:index+100])
        # print("--------------------")

    return currentDiskMap

def computeChecksum(compactedDiskMap):
    checksum = 0
    for i in range(len(compactedDiskMap)):
        checksum += i * compactedDiskMap[i]
    return checksum

diskMap = createDiskMap(disk)
compactedDiskMap = compactDiskPart1(diskMap)
compactedDiskChecksum = computeChecksum(compactedDiskMap)
print("Part 1:", compactedDiskChecksum)

def compactDiskPart2(diskMap):
    # A list containing the indices of diskMap corresponding to free space
    currentDiskMap = copy.deepcopy(diskMap)
    
    # Three questions:
    # (1) which file do we want to move?
    # (2) how big is the file?
    # (3) how much free space do we have, and will the file fit in that free space?

    # Maps index -> the number of free spaces available, starting at that index until
    # the next allocated space
    freeSpaceRange = {}
    i = 0
    while i < len(currentDiskMap):
        # If we're at a free space
        if currentDiskMap[i] == None:
            # Count the number of free spaces available at
            # this index, until the next allocated space
            j = i
            while currentDiskMap[j] == None:
                j += 1
                if j >= len(currentDiskMap):
                    break
            freeSpaceRange[i] = j-i
            print("Found {} free spaces at index {}".format(j-i, i))
            i = j
        else:
            i += 1
    
    print(freeSpaceRange)
    
    fileToMove = currentDiskMap[-1]
    


    
    """
    freeSpaceRange = {2: 3, 8: 3, 12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}
    Move file 9
    freeSpaceRange = {4: 1, 8: 3, 12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}
    

    
    """

    # A map telling us the size of each file
    fileSize = Counter(currentDiskMap)
    print(fileSize)
    
    return currentDiskMap

diskMap = createDiskMap(disk)
#print("Disk map:", diskMap)
compactedDiskMap = compactDiskPart2(diskMap)
print("Compacted disk map:", compactedDiskMap)
compactedDiskChecksum = computeChecksum(compactedDiskMap)
print("Part 2:", compactedDiskChecksum)