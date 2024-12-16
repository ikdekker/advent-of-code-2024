import heapq

walls = set()
reindeer = None
goal = None
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # directions: U, R, D, L
map = []

with open("inputs/16_1.txt") as file:
    for y, line in enumerate(file):
        row = line.strip()
        map.append(row)
        for x, char in enumerate(row):
            if char == '#':
                walls.add((x, y))
            elif char == 'S':
                reindeer = (x, y, 1) # Start facing east, index 1 in dirs
            elif char == 'E':
                goal = (x, y)

def find_min_score(start, goal):
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], start[2]))
    visited = set()
    while pq:
        score, x, y, d = heapq.heappop(pq)

        if (x, y) == goal:
            return score

        if (x, y, d) in visited:
            continue
        visited.add((x, y, d))

        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if (nx, ny) not in walls:
            heapq.heappush(pq, (score + 1, nx, ny, d))

        new_d = (d - 1) % 4
        if (x, y, new_d) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_d))

        new_d = (d + 1) % 4
        if (x, y, new_d) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_d))

result = find_min_score(reindeer, goal)
print("Lowest Score:", result)