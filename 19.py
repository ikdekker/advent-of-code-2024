def solve(design, stripes, read_from, idx_reachable):
    if read_from in idx_reachable:
        return idx_reachable[read_from]
    if  read_from == len(design):
        return True
    for stripe in stripes:
        read_to = read_from+len(stripe)
        if design[read_from:read_to] == stripe:
            if solve(design, stripes, read_to, idx_reachable):
                idx_reachable[design[0:read_to]] = True
                return True
    idx_reachable[read_from] = False
    return False
with open("inputs/19_1.txt") as file:
    lines = file.read().strip().splitlines()
    stripes = set(lines[0].strip().split(", "))
    designs = lines[2:]

print(sum([solve(design, stripes, 0, {}) for design in designs])) #rrbgbr
# for design in designs:
#     print(design)
#     print(sum([solve(design, stripes, 0)]))

