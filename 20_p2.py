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
# print(path)
diffs = []
c=0
for p, score in path.items():
    cheat_options = []
    for x_d in range(-RANGE,RANGE+1):
        for y_d in range(-RANGE, RANGE+1):
            if abs(x_d) + abs(y_d) > RANGE:
                continue
            cheatx, cheaty = p[0] + x_d, p[1] + y_d
            if (cheatx, cheaty) in path:
                # cheat is allowed
                cheat_path_len = abs(x_d) + abs(y_d) # manhattan dist taken to get to the next tile
                diff = path[(cheatx, cheaty)] - score - cheat_path_len
                # print("new IS in p", diff)
                if diff >= 100:
                    c += 1
                    # print("cheat:", p, (cheatx,cheaty), "vals", score, path[(cheatx, cheaty)], diff, c)
                    diffs.append(diff)
print(len(diffs)) #348741