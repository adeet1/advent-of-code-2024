import itertools

puzzle = []
with open("input/day7.txt", "r") as file:
    for line in file:
        tmp = line.split(":")
        values = tmp[1].split(" ")
        newRow = [tmp[0]] + values[1:]
        puzzle.append([int(x) for x in newRow])

def executeRow(testValue, operands):
    operatorCombos = list(itertools.product(["+", "*"], repeat=len(operands)-1))
    
    for operatorCombo in operatorCombos:
        expression = str(operands[0]) + operatorCombo[0] + str(operands[1])

        for i in range(1, len(operatorCombo)):
            expression = "(" + expression + ")" + operatorCombo[i] + str(operands[i+1])
        
        # print("Expected", testValue, "but was:", eval(expression), "=", expression)

        if testValue == eval(expression):
            return True
    
    return False

totalCalibrationResult = 0
for row in puzzle:
    testValue = row[0]
    operands = row[1:]

    if executeRow(testValue, operands):
        totalCalibrationResult += testValue

print("Part 1:", totalCalibrationResult)