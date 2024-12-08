total = 0
operators = "*+"

def match_target(ops, current_sum, target):
    if current_sum == target:
        print(target)
        return target
    if len(ops) == 0:
        return 0
    if current_sum < target:
        return match_target(ops[1:], current_sum + ops[0], target) + match_target(ops[1:], current_sum * ops[0], target)
    return 0

with open("inputs/7.txt") as file:
    for line in file:
        input_str = line.strip().split(": ")
        print(input_str)
        target = int(input_str[0])
        operands = list(map(int, input_str[1].split(" ")))
        if match_target(operands, 0, target) > 0:
            total += target

print(total)