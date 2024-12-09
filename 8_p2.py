nodes_placed = n = m = 0
obs = {}
all_ants={}
def is_in_bounds(x, y):
    global m,n
    return 0 <= x < m and 0 <= y < n

outx = []
with open("inputs/8.txt") as file:
    for y, line in enumerate(file):
        m = y + 1
        outx.append([])
        for x, c in enumerate(line.strip()):
            n = x + 1
            if c != ".":
                obs[c] = obs.get(c, []) + [(x,y)]
                all_ants[((x,y))] = c
                outx[y].append("📡")
            else:
                outx[y].append('⏹️')
seen = set()
nodes = set()
for k, antennae in obs.items():
    for ant in antennae:
        for ant_2 in antennae:
            a_id = str(ant) + str(ant_2)
            a_id_x = str(ant_2) + str(ant)
            if a_id in seen:
                continue
            if ant == ant_2:
                nodes.add(ant)
                continue
            seen.add(a_id)
            seen.add(a_id_x)

            delta = (ant_2[0] - ant[0], ant_2[1] - ant[1])
            x1, y1, x2, y2 = ant[0] - delta[0], ant[1] - delta[1], ant_2[0] + delta[0], ant_2[1] + delta[1]
            while is_in_bounds(x1, y1):
                nodes.add((x1, y1))
                outx[y1][x1] = "🎄"
                x1, y1 = x1-delta[0], y1-delta[1]
            while is_in_bounds(x2, y2):
                nodes.add((x2, y2))
                outx[y2][x2] = "🎄"
                x2, y2 = x2+delta[0], y2+delta[1]

for y in range(n):
    print()
    for x in range(m):
        print(outx[y][x], end='')
print()
print(len(nodes))

