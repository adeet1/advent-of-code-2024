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
    if a == 0:
        return b

    return int(str(a) + str(b))

def executeRow(testValue, operands):
    # print("Operands:", operands)
    operatorCombos = list(itertools.product(["+", "*", "||"], repeat=len(operands)-1))
    
    for operatorCombo in operatorCombos:
        expression = str(operands[0])
        # if operatorCombo[0] == "||":
        #     expression = re.sub(r"(\d+)\s*\|\|\s*(\d+)", r"concat_operator(\1, \2)", expression)

        print("Evaluating starting expression", expression)

        for i in range(len(operatorCombo)):
            # forgot to put str(eval) and just did eval which is why i got int str concat errors
            tmp = eval("(" + expression + ")", {"concat_operator": concat_operator})
            expression = str(tmp) + operatorCombo[i] + str(operands[i+1])

            if operatorCombo[i] == "||":
                expression = re.sub(r"(\d+)\s*\|\|\s*(\d+)", r"concat_operator(\1, \2)", expression)

            print("Evaluating expression:", testValue, "?=", expression)
            if testValue == eval(expression, {"concat_operator": concat_operator}):
                print("----", testValue, "validates ----")
                return True
    
    return False

totalCalibrationResult = 0
for row in puzzle:
    testValue = row[0]
    operands = row[1:]

    if executeRow(testValue, operands):
        totalCalibrationResult += testValue

print("Part 2:", totalCalibrationResult) # 509463489905922 is too high