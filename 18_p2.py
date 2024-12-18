
def solve(bits):
    dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # directions: U, R, D, L
    GRID_SIZE = 71
    q = [(0,0,0)]
    v = set()
    while q:
        (x,y,depth) = q.pop(0)
        if x == GRID_SIZE - 1 and y == GRID_SIZE - 1:
            return depth
        if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            continue
        if (x, y) in v:
            continue
        v.add((x, y))
        if (x, y) in bits:
            continue

        for d in dirs:
            dx, dy = d
            if not (x + dx, y + dy) in bits and x >= 0 and y >= 0 and x < GRID_SIZE and y < GRID_SIZE:
                q.append((x + dx, y + dy, depth+1))

    return -1


bits = []
with open("inputs/18_1.txt") as file:
    for c, line in enumerate(file):
        bit = int(line.strip().split(",")[0]),int(line.strip().split(",")[1])
        bits.append(bit)
        if c == 1023:
            break
bitset = set()
for b in bits:
    bitset.add(b)
g = 71