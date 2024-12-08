def match_target(ops, current_sum, target):
    global is_part2
    if len(ops) == 0:
        return current_sum == target
    if current_sum <= target:
        part1_mult = match_target(ops[1:], current_sum * ops[0], target)
        if part1_mult:
            return 1
        part1_add = match_target(ops[1:], current_sum + ops[0], target)
        if part1_add:
            return 1
        part2_concat = match_target(ops[1:], int(str(current_sum) + str(ops[0])), target)
        if part2_concat:
            return is_part2
    return 0

total, is_part2 = 0, True
with open("inputs/7.txt") as file:
    for line in file:
        input_str = line.strip().split(": ")
        target = int(input_str[0])
        operands = list(map(int, input_str[1].split()))
        if match_target(operands[1:], operands[0], target) > 0:
            total += target
print(total)