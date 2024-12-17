from time import sleep


def operand_value(operand,registers):
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


# def r_execute_program(program, )

def execute_program(program, registers, iptr, output):
    set_of_candidates = set()
    while iptr < len(program):
        # sleep(1)
        op = program[iptr]
        operand = program[iptr + 1]
        # if op == 5:
            # print("using operand " + str(operand_value(operand, registers)%8), "4=A,5=B=6=C")
        # print(str(op) + ":" + str(operand), end='')
        # print(registers)
        if op == 0:  # adv
            # print(" div reg A by", 2 ** operand_value(operand,registers))
            registers[0] //= 2 ** operand_value(operand,registers)
            # means the value was halved by the square of the operand, to restore, we can use
            # e.g. 8 // 2** 2 == 2, can be recovered by 2*2*2
            # 16, 3 = 1 = 1 not invertable?
            # input 9 until 17 would be 1 for operand 3.
            # multiplication, by the 1*8
            # return {registers[0] * i for i in [1,4,9,16,25,36,49]}
        elif op == 1:  # bxl
            # print(" XOR reg B with operand (L)", operand)
            registers[1] ^= operand # inversion is the same
        elif op == 2:  # bst
            # print(" set reg B", operand_value(operand,registers) % 8)
            registers[1] = operand_value(operand,registers) % 8 # lost info, not invertable, but we can multiply by 8
        elif op == 3:  # jnz
            if registers[0] != 0:
                # print(" jumping to iptr! from:to",iptr,operand)
                iptr = operand
                continue
        elif op == 4:  # bxc
            # print(" setting XOR B ^= C", registers[1],registers[2], end="")
            registers[1] ^= registers[2]
            # print(" output:", registers[1])
        elif op == 5:  # out
            # print(" PRINT:", operand_value(operand,registers) % 8)
            # print("opval", operand, operand_value(operand,registers))
            output.append(operand_value(operand,registers) % 8)
            # probably important as this will have to become 2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
            # with the first op being 2, so we need to print 2
            #
        elif op == 6:  # bdv
            # print(" DIV reg A/Opreg:", registers[0] // (2 ** operand_value(operand,registers)))
            registers[1] = registers[0] // (2 ** operand_value(operand,registers))
        elif op == 7:  # cdv
            # print(" DIV reg C=A/Opreg:",registers[0] // (2 ** operand_value(operand,registers)))
            registers[2] = registers[0] // (2 ** operand_value(operand,registers))
        # print("registers:",registers)
        iptr += 2

    return output

def test_out(out):
    expected = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]
    first_n = 0
    for i in enumerate(expected):
        print(i)
        first_n += out[i] == expected[i]
    return first_n

def calc_next(regs):
    A1 = regs[0]
    B1 = (A1 % 8)
    B2 = B1 ^ 5
    B3 = B2 ^ 6
    C1 = A1 // (2 ** B2)
    A2 = A1 // 8
    B4 = B3 ^ C1
    # print(B1, B2,B3,B4, C1)
    return B4, [A2,B4,C1]

def test_char(c, idx):
    # register A holds the value that will be printed
    chars = [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0]
    return c % 8 == chars[idx]


from concurrent.futures import ThreadPoolExecutor
import itertools


def worker(start, end, step):
    prev = 0
    c = 1
    for i in range(end, start, -1):
        if c % 1000000 == 0:
            print("Thread:", start, "checked", c // 1000000, "M %")
        c += 1
        char = 0
        regs = [i, 0, 0]
        while char < 16:
            res = calc_next(regs)
            out_c = res[0]
            regs = res[1]
            if not test_char(out_c, char):
                break
            char += 1

        if char > 12:
            print("Thread:", start, char, i)
            print("DIFF", i - prev)
            prev = i
        if char == 16:
            print("FOUND SOLUTION", i)
            out = execute_program(program, [i, 0, 0], 0, [])
            print(out, len(out))
            exit()


def in_gen():
    lower_bnd = 101526679218586 # 99472133663130 #99472133679514 #35268815055258 # 35184439552410 # 104145058146714 # 35187210824090
    higher_bnd = 105981155568026 # 105981156665754
    step = 98304 # 16384 # 98304
    total_range = range(lower_bnd, higher_bnd, step)
    num_threads = 1  # Number of threads

    chunk_size = len(total_range) // num_threads
    print("amount to check:", len(total_range) // 1000000, "million")

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Split range into chunks for threads
        futures = []
        for i in range(1, num_threads + 1):
            start = lower_bnd + i * chunk_size * step
            end = lower_bnd + (i + 1) * chunk_size * step
            futures.append(executor.submit(worker, start, end, step))

        for future in futures:
            future.result()

in_gen()
"""
goal
[0, 0, 0]
2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0
"""
