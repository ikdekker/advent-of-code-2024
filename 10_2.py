from pydoc import visiblename

m = n = 0
map = []

# Reading the input map from the file
with open("inputs/10_1.txt") as file:
    for y, line in enumerate(file):
        n = y + 1
        map.append([])
        for x, o in enumerate(line.strip()):
            m = x + 1
            map[y].append(int(o))


def count(x,y,m,n,map,visited,nines,expected):
    if x < 0 or x >= m or y < 0 or y >= n or expected != map[x][y]:
        return 0
    if map[x][y] == 9:
        return 1
    if visited[x][y]:
        return nines[x][y]

    return sum(
            [count(x + 1,y,m,n,map,visited,nines,expected+1),
            count(x - 1, y, m, n, map, visited,nines,expected+1),
            count(x, y + 1, m, n, map, visited,nines,expected+1),
            count(x, y - 1, m, n, map, visited,nines,expected+1)]
        )

visited = [[False for x in range(m)] for y in range(n)]
nines_reachable = [[0 for x in range(m)] for y in range(n)]
print(sum(count(x,y,m,n,map,visited,nines_reachable, 0) for x in range(m) for y in range(n)))