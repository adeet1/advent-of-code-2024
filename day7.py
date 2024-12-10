import itertools
import re

puzzle = []
with open("input/day7.txt", "r") as file:
    for line in file:
        tmp = line.split(":")
        values = tmp[1].split(" ")
        newRow = [tmp[0]] + values[1:]
        puzzle.append([int(x) for x in newRow])

def concat_operator(a, b):
    return str(a) + str(b)

def executeRow(testValue, operands):
    print("operands =", operands)
    operatorCombos = list(itertools.product(["+", "*", "||"], repeat=len(operands)-1))
    
    for operatorCombo in operatorCombos:
        expression = str(operands[0]) + operatorCombo[0] + str(operands[1])
        if operatorCombo[0] == "||":
            expression = re.sub(r"(\d+)\s*\|\|\s*(\d+)", r"concat_operator(\1, \2)", expression)

        print("Evaluating starting expression", expression)

        for i in range(1, len(operatorCombo)):
            # forgot to put str(eval) and just did eval which is why i got int str concat errors
            expression = str(eval("(" + expression + ")")) + operatorCombo[i] + str(operands[i+1])

            if operatorCombo[i] == "||":
                expression = re.sub(r"(\d+)\s*\|\|\s*(\d+)", r"concat_operator(\1, \2)", expression)

            print("Evaluating expression:", testValue, "?=", expression)
            if testValue == eval(expression):
                print("----", testValue, "validates ----")
                return True
    
    return False

totalCalibrationResult = 0
for row in puzzle:
    testValue = row[0]
    operands = row[1:]

    if executeRow(testValue, operands):
        totalCalibrationResult += testValue

print("Part 1:", totalCalibrationResult)