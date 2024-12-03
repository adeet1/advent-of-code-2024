import re

# Use regex to filter down only to text in the format mul(X,Y)
regex = "mul\(\d+,\d+\)"

lines = []
with open("input/day3.txt", "r") as file:
    lines = [line for line in file]

mults_list = list(map(lambda line: re.findall(regex, line), lines))

result = 0
for mults in mults_list:
    # For each instruction, extract the two numbers and multiply them
    for mult in mults:
        numbers = mult[:-1].split("(")[-1]
        a, b = numbers.split(",")
        result += int(a) * int(b)

print("Part 1:", result)

regex = "(?:do\(\))|(?:don't\(\))|mul\(\d+,\d+\)"

mults_list = list(map(lambda line: re.findall(regex, line), lines))

result = 0
multEnabled = True
for mults in mults_list:
    # For each instruction, extract the two numbers and multiply them
    for mult in mults:
        if mult == "do()":
            multEnabled = True
            continue
        elif mult == "don't()":
            multEnabled = False
            continue

        if multEnabled:
            numbers = mult[:-1].split("(")[-1]
            a, b = numbers.split(",")
            result += int(a) * int(b)

print("Part 2:", result)
