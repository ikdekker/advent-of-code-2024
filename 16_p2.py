import copy
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
                reindeer = (x, y, 1)  # Start facing east, index 1 in dirs
            elif char == 'E':
                goal = (x, y)

def find_min_score(start, goal):
    pq = []
    ps = set()
    ps.add((start[0], start[1]))
    heapq.heappush(pq, (0, start[0], start[1], start[2], ps))
    min_score = 999999999999
    visited = {}
    best_paths_vis = set()
    while pq:
        score, x, y, d, p = heapq.heappop(pq)
        if score > min_score:
            continue
        if (x, y) == goal:
            if score < min_score:
                min_score = score
                best_paths_vis = p # new best path, wipe all others
                continue
            elif score == min_score:
                best_paths_vis.update(p)
            continue

        if (x, y, d) in visited and visited[(x, y, d)] < score:
            continue
        visited[(x, y, d)] = score

        nx, ny = x + dirs[d][0], y + dirs[d][1]
        if (nx, ny) not in walls:
            dp = copy.copy(p)
            dp.add((nx, ny))
        if (nx, ny) not in walls and (nx, ny, d) not in visited:
            heapq.heappush(pq, (score + 1, nx, ny, d, dp))


        new_d = (d + 1) % 4
        if (x, y, new_d) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_d, p))
        new_d = (d - 1) % 4
        if (x, y, new_d) not in visited:
            heapq.heappush(pq, (score + 1000, x, y, new_d, p))

    return min_score, best_paths_vis

result, v = find_min_score(reindeer, goal)
print("Lowest Score:", result, len(v))

# def print_wh_entry(pos,bot, walls, vis, emoji):
#     if pos == bot:
#         return "🤖" if emoji else '@'
#     elif pos in walls:
#         return '🧱' if emoji else '#'
#     elif pos in vis:
#         return '🍊' if emoji else 'V'
#     return "🌔" if emoji else '.'
#
# def print_wh(warehouse_map, walls,vis, bot):
#     for y, row in enumerate(warehouse_map):
#         row_output = []
#         for x, char in enumerate(row):
#             pos = (x, y)
#             use_emoji = len(warehouse_map[0]) < 40 or True
#             c = print_wh_entry(pos,bot, walls, vis,use_emoji)
#             row_output.append(c)
#         print(''.join(row_output))
#
# print_wh(map,walls, v, reindeer)