import itertools

puzzle = []
with open("input/day7.txt", "r") as file:
    for line in file:
        tmp = line.split(":")
        values = tmp[1].split(" ")
        newRow = [tmp[0]] + values[1:]
        puzzle.append([int(x) for x in newRow])

def executeRow(testValue, operands):
    print("operands =", operands)
    operatorCombos = list(itertools.product(["+", "*", "||"], repeat=len(operands)-1))
    
    for operatorCombo in operatorCombos:
        if operatorCombo[0] == "||":
            expression = "'" + str(operands[0]) + "'+'" + str(operands[1]) + "'"
        else:
            expression = str(operands[0]) + operatorCombo[0] + str(operands[1])
        
        print("Starting expression:", expression)

        for i in range(1, len(operatorCombo)):
            if operatorCombo[i] == "||":
                expression = "'" + str(eval(expression)) + "'+'" + str(operands[i+1]) + "'"
                print("concat expression:", expression)
            else:
                expression = "(" + expression + ")" + operatorCombo[i] + str(operands[i+1])
            print("Expression:", expression)
            
            print("Evaluated to", eval(expression))
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