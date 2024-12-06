from xml.sax.saxutils import escape

obstacles = set()
visited = set()
guard = [0, 0]
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

visited.add(guard)
while True:
    dx = dirs[d][0]
    dy = dirs[d][1]
    new_guard_pos = (guard[0] + dx, guard[1]+ dy)
    if new_guard_pos[0] in {-1, m} or new_guard_pos[1] in {-1, n}: # OoB
        break
    if new_guard_pos in obstacles:
        d = (d + 1) % 4
        continue

    guard = new_guard_pos
    visited.add((guard[0],guard[1]))

print(len(visited))