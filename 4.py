def recurse(grid, x, y, step, m, n, direction = None):
    exploration_grid = []
    for i in range(-1,2):
        for j in range(-1,2):
            exploration_grid.append([i,j])
    sum = 0
    for d in exploration_grid:
        x_new = x + d[0]
        y_new = y + d[1]
        if x_new >= m or x_new < 0 or y_new >= n or y_new < 0:
            continue
        if grid[y_new][x_new] == "XMAS"[step] and (not direction or d==direction):
            sum += 1 if step == 3 else recurse(grid, x_new, y_new, step + 1, m, n, d)
    return sum

grid = []
with open("inputs/4.txt") as file:
    for line in file:
        row = []
        grid.append(list(line.strip()))
# M x N grid
m = len(grid[0])
n = len(grid)
xmas_count = 0

for y in range(n):
    for x in range(m):
        if grid[y][x] == 'X':
            xmas_count += recurse(grid, x, y, 1, m, n)

print(xmas_count)