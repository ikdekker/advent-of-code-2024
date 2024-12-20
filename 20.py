from itertools import count

walls = set()
reindeer = None
goal = None
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # directions: U, R, D, L
map = []

with open("inputs/20_1.txt") as file:
    for y, line in enumerate(file):
        row = line.strip()
        map.append(row)
        for x, char in enumerate(row):
            if char == '#':
                walls.add((x, y))
            elif char == 'S':
                reindeer = (x, y)
            elif char == 'E':
                goal = (x, y)

def find_min_score(start, goal):
    path = {}
    pos = (start[0],start[1])
    d = 0
    while not pos == goal:
        x, y = pos
        path[(x,y)] = len(path)
        # continue straight
        nx, ny = x + dirs[d][0], y + dirs[d][1]
        new_d = d
        if (nx, ny) in walls:
            new_d = (d - 1) % 4
            nx, ny = x + dirs[new_d][0], y + dirs[new_d][1]
        if (nx, ny) in walls:
            new_d = (d + 1) % 4
            nx, ny = x + dirs[new_d][0], y + dirs[new_d][1]
        if pos == (nx,ny):
            print("stuck")
            break
        pos = (nx,ny)
        d = new_d
        print(pos,d)
    return path


path = find_min_score(reindeer, goal)
path[goal] = len(path)
print("Path len:", len(path))
print(path)
diffs = []
c=0
for p, score in path.items():
    # check all dirs, if two steps in the directions are not a wall, we can skip there
    for d in dirs:
        cheatx2, cheaty2 = p[0] + d[0]*2, p[1] + d[1]*2
        # print("cheat", reindeer, (cheatx2,cheaty2))
        if (cheatx2, cheaty2) in path:
            diff = path[(cheatx2, cheaty2)] - score - 2
            # print("new IS in p", diff)
            if diff >= 100:
                c += 1
                print("cheat:", p, (cheatx2,cheaty2), "vals", score, path[(cheatx2, cheaty2)], diff, c)
                diffs.append(diff)
print(len(diffs))