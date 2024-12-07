obstacles = set()
guard = (0, 0)
n = m = 0
d = -1
dirs = [[0,-1], [1,0], [0,1], [-1,0]] # directions: U, R, D, L
dirs_chars = "^>v<"

with open("inputs/6.txt") as file:
    for y, line in enumerate(file):
        n = y + 1
        for x, o in enumerate(line.strip()):
            m = x + 1
            if o == '#':
                obstacles.add((x,y))
            if d == -1:
                d = dirs_chars.find(o)
                guard = (x, y)


def walk_and_obstruct(obstacles, guard, m, n, d, dirs, extra_obstacle):
    visited = {guard: d}
    total = 0
    tried = set()
    while True:
        dx = dirs[d][0]
        dy = dirs[d][1]
        new_guard_pos = (guard[0] + dx, guard[1] + dy)
        if extra_obstacle == (-1,-1) and new_guard_pos not in tried:
            tried.add(new_guard_pos)
            total += walk_and_obstruct(obstacles, guard, m, n, d, dirs, new_guard_pos)
        if new_guard_pos in visited and visited[new_guard_pos] == d:
            return 1

        if new_guard_pos[0] in {-1, m} or new_guard_pos[1] in {-1, n}:  # OoB
            return total
        if new_guard_pos in obstacles.union({extra_obstacle}):
            d = (d + 1) % 4
            continue

        guard = new_guard_pos
        visited[guard] = d
    return total



print(walk_and_obstruct(obstacles, guard, m, n, d, dirs, (-1,-1)))
