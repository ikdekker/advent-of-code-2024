# Reading the input map from the file
with open("inputs/12_1.txt") as file:
    garden = [list(line.strip()) for line in file]
n = len(garden)
m = len(garden[0]) if garden else 0

def sum_tuples(gen):
    return tuple(map(sum, zip(*gen))) if gen else (0, 0)


def tuple_to_price(t):
    return t[0] * t[1]

def count_perimeter(i, j, m, n, A, plant, garden, visited, patch):
    if i < 0 or i >= n or j < 0 or j >= m or plant != garden[i][j]:
        return None
    if visited[i][j]:
        return True
    if patch == -1:
        patch = (i, j)
        A[(plant, patch)] = {}
    if (i, j) in A[(plant, patch)]:
        return A[(plant, patch)][(i, j)]

    visited[i][j] = True

    neighbors = [
        count_perimeter(i + 1, j, m, n, A, plant, garden, visited, patch),
        count_perimeter(i - 1, j, m, n, A, plant, garden, visited, patch),
        count_perimeter(i, j + 1, m, n, A, plant, garden, visited, patch),
        count_perimeter(i, j - 1, m, n, A, plant, garden, visited, patch)
    ]

    local_perimeter = 4
    for f in neighbors:
        local_perimeter -= bool(f)

    A[(plant, patch)][(i, j)] = (1, local_perimeter)
    return A[(plant, patch)][(i, j)]

A = {}
visited = [[False for _ in range(m)] for _ in range(n)]

[count_perimeter(i, j, m, n, A, garden[i][j], garden, visited, -1) for i in range(n) for j in range(m)]

plant_sums = {}
for plant_key, patch in A.items():
    plant_type = plant_key[0]
    patch_root = plant_key[1]
    if (plant_type,patch_root) not in plant_sums:
        plant_sums[(plant_type,patch_root)] = (0, 0)
    plant_sums[(plant_key, patch_root)] = sum_tuples(patch.values())

# Calculate prices and sum them
combined_prices = sum(tuple_to_price(total) for total in plant_sums.values())

print(combined_prices)
