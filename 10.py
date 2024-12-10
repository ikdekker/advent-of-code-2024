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

def count(i, j, m, n, map, visited, expected):
    if i < 0 or i >= n or j < 0 or j >= m or expected != map[i][j]:
        return set()
    if map[i][j] == 9:
        return {i*m+j}
    if visited[i][j]:
        return visited[i][j]

    visited[i][j] = set().union(
        count(i + 1, j, m, n, map, visited, expected + 1),
         count(i - 1, j, m, n, map, visited, expected + 1),
         count(i, j + 1, m, n, map, visited, expected + 1),
         count(i, j - 1, m, n, map, visited, expected + 1)
    )
    return visited[i][j]

visited = [[False for i in range(m)] for j in range(n)]

print(sum(len(count(x,y,m,n,map,visited, 0)) for x in range(m) for y in range(n)))