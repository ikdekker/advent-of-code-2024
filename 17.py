registers = [0,0,0]
iptr = 0
output = []

def operand_value(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return registers[0]
    elif operand == 5:
        return registers[1]
    elif operand == 6:
        return registers[2]
    print("7 used?")
    exit(1)

with open("inputs/17.txt") as file:
    lines = file.read().strip().splitlines()
    registers[0] = int(lines[0].split(":")[1].strip())  # A
    registers[1] = int(lines[1].split(":")[1].strip())  # B
    registers[2] = int(lines[2].split(":")[1].strip())  # C
    program = list(map(int, lines[4].split(":")[1].strip().split(",")))


while iptr < len(program):
    op = program[iptr]
    operand = program[iptr + 1]
    print(registers)
    if op == 0:  # adv
        registers[0] //= 2 ** operand_value(operand)
    elif op == 1:  # bxl
        registers[1] ^= operand
    elif op == 2:  # bst
        registers[1] = operand_value(operand) % 8
    elif op == 3:  # jnz
        if registers[0] != 0:
            iptr = operand
            continue
    elif op == 4:  # bxc
        registers[1] ^= registers[2]
    elif op == 5:  # out
        output.append(operand_value(operand) % 8)
    elif op == 6:  # bdv
        registers[1] = registers[0] // (2 ** operand_value(operand))
    elif op == 7:  # cdv
        registers[2] = registers[0] // (2 ** operand_value(operand))

    iptr += 2


print(",".join(map(str, output)))
