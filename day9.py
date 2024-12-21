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
    isFreeSpace = [diskMap[_] == None for _ in range(len(diskMap))]
    currentDiskMap = copy.deepcopy(diskMap)
    index = 0
    
    # Three questions:
    # (1) which file do we want to move?
    # (2) how big is the file?
    # (3) how much free space do we have, and will the file fit in that free space?

    # A map telling us the size of each file
    fileSize = Counter(currentDiskMap)
    print(fileSize)
    lastFileIndex = len(currentDiskMap)-1

    while index < len(currentDiskMap):
        lastFileId = currentDiskMap[lastFileIndex]
        lastFileSize = fileSize[lastFileId]
        print("Current disk map:", currentDiskMap)
        print("Last file is at index {} - it has id {} and size {}".format(lastFileIndex, lastFileId, lastFileSize))
        print("index =", index, ": file block =", currentDiskMap[index], ": is free space =", isFreeSpace[index])

        if isFreeSpace[index]:
            # Count the number of free spaces at this index
            freeSpaceIndex = index
            while currentDiskMap[freeSpaceIndex] == None:
                freeSpaceIndex += 1
                
                # Stop the loop so that we don't go out of bounds
                # if the rest of the array consists of free spaces
                if freeSpaceIndex == len(currentDiskMap):
                    break
            
            numFreeSpacesAtThisIndex = freeSpaceIndex - index
            print("Found {} free spaces at index {}".format(numFreeSpacesAtThisIndex, index))

            # If there's enough free space for us to move the file here
            if lastFileSize <= numFreeSpacesAtThisIndex:
                print("Moving file", lastFileId, "to these free spaces")
                # Copy the file here
                currentDiskMap[index:index+lastFileSize] = [lastFileId] * lastFileSize

                # Mark these spaces as allocated
                isFreeSpace[index:index+lastFileSize] = [False] * lastFileSize

                # Remove the file from the space where it was allocated previously
                for _ in range(lastFileSize):
                    currentDiskMap[lastFileIndex-_] = None
                    isFreeSpace[lastFileIndex-_] = True

                index += 1
            else:
                print("File", lastFileId, "can't fit here")
                # The file couldn't fit, so we can't allocate it here
                # But stay here in case we find another file that fits here
                pass

            lastFileIndex -= lastFileSize
            # In case the lastFileIndex is at a free space, keep rewinding
            # it until it's pointing at a file
            while currentDiskMap[lastFileIndex] == None:
                lastFileIndex -= 1
        else:
            index += 1
        print("====================================")
    
    return currentDiskMap

diskMap = createDiskMap(disk)
#print("Disk map:", diskMap)
compactedDiskMap = compactDiskPart2(diskMap)
print("Compacted disk map:", compactedDiskMap)
compactedDiskChecksum = computeChecksum(compactedDiskMap)
print("Part 2:", compactedDiskChecksum)