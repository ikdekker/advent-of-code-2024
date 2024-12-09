nodes_placed = n = m = 0
obs = {}

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
            outx[y].append(c)
seen = set()
nodes = set()
for k, antennae in obs.items():
    for ant in antennae:
        for ant_2 in antennae:
            a_id = str(ant) + str(ant_2)
            a_id_x = str(ant_2) + str(ant)
            if ant == ant_2 or a_id in seen:
                continue
            seen.add(a_id)
            seen.add(a_id_x)
            print(seen)
            delta = (ant_2[0] - ant[0], ant_2[1] - ant[1])
            if is_in_bounds(ant[0] - delta[0], ant[1] - delta[1]):
                nodes.add((ant[0] - delta[0], ant[1] - delta[1]))
                print(ant[0] - delta[0], ant[1] - delta[1])
                print(outx[ant[1] - delta[1]][ant[0] - delta[0]])
                outx[ant[1] - delta[1]][ant[0] - delta[0]] = "#"
            if is_in_bounds(ant_2[0] + delta[0], ant_2[1] + delta[1]):
                nodes.add((ant_2[0] + delta[0], ant_2[1] + delta[1]))
                print(ant_2[0] + delta[0], ant_2[1] + delta[1])
                print(outx[ant_2[1] + delta[1]][ant_2[0] + delta[0]])
                outx[ant_2[1] + delta[1]][ant_2[0] + delta[0]] = "#"

for y in range(n):
    print()
    for x in range(m):
        print(outx[y][x], end='')
print()
print(len(nodes))
