input_str = open("inputs/3.txt", "r").read()

mul_marker = 0
do_marker = 0
dont_marker = 0
nr_str1 = ""
nr_str2 = ""
total_mul = 0
found_comma = False
doing = True

def reset_and_add():
    global nr_str1, nr_str2, total_mul, found_comma
    if nr_str1.isnumeric() and nr_str2.isnumeric():
        total_mul += int(nr_str1) * int(nr_str2)
    nr_str1 = ""
    nr_str2 = ""
    found_comma = False

def reset(to_marker):
    global nr_str1, nr_str2, mul_marker, found_comma
    nr_str1 = ""
    nr_str2 = ""
    found_comma = False
    mul_marker = to_marker

for c in input_str:
    if doing:
        if dont_marker < 7 and c == "don't()"[dont_marker]:
            dont_marker += 1
            if dont_marker == 7:
                doing = False # True for part 1
                do_marker = 0
                reset(c == 'm')
                continue
        else:
            dont_marker = c == 'd'

        if mul_marker == 4:
            if c == ")": # final character, nr_2 must
                if nr_str2:
                    mul_marker = 0
                    reset_and_add()
                    continue
            if c == "," and nr_str1:
                if not found_comma:
                    found_comma = True
                else:
                    reset(c == 'm')
            elif c.isdigit():
                if not found_comma:
                    nr_str1 += c
                else:
                    nr_str2 += c
            elif not c.isdigit():
                reset(c == 'm')
        elif mul_marker < 4 and c == "mul("[mul_marker]:
            mul_marker += 1
        else:
            if mul_marker > 0 and mul_marker < 4:
                mul_marker = int(c == 'm')  # Reset if partial "mul(" is followed by invalid input
    else:
        if do_marker < 4 and c == "do()"[do_marker]:
            do_marker += 1
        else:
            if do_marker != 4:
                do_marker = c == 'd'
            else:
                doing = do_marker == 4
                dont_marker = 0


print(total_mul)
