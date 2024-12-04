def check_corners(grid, x, y, m, n, direction = None):
    """
    I'm checking an X shape:
    B . C
    . A .
    D . E
    Where the B+E = "SM|MS" && C+D = "SM|MS"
    """
    if x < 1 or x >= m - 1 or y < 1 or y >= n- 1:
        return 0
    print(x,y)
    B = grid[y-1][x-1]
    C = grid[y-1][x+1]
    D = grid[y+1][x-1]
    E = grid[y+1][x+1]
    return (B+E == "SM" or B+E == "MS") and (C+D == "SM" or C+D == "MS")

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
        if grid[y][x] == 'A':
            xmas_count += check_corners(grid, x, y, m, n)

print(xmas_count)