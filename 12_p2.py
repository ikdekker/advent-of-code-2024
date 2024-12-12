# Reading the input map from the file
with open("inputs/12_1.txt") as file:
    garden = [list(line.strip()) for line in file]
n = len(garden[0]) if garden else 0
m = len(garden)

def count_perimeter(i, j, m, n, A, plant, garden, visited, patch):
    if i < 0 or i >= n or j < 0 or j >= m or plant != garden[i][j]:
        return None
    if visited[i][j]:
        return True # doesn't matter what is returned, as long as its not None
    if patch == -1: # uniqueness property of a patch, is the starting location, I also store the plant, not particularly useful
        patch = (i, j)
        A[(plant, patch)] = {}
    if (i, j) in A[(plant, patch)]:
        return A[(plant, patch)][(i, j)]

    visited[i][j] = True # could be replaced by a check if the plant == expected_plant

    neighbors = [
        count_perimeter(i + 1, j, m, n, A, plant, garden, visited, patch),
        count_perimeter(i - 1, j, m, n, A, plant, garden, visited, patch),
        count_perimeter(i, j + 1, m, n, A, plant, garden, visited, patch),
        count_perimeter(i, j - 1, m, n, A, plant, garden, visited, patch)
    ]
    # DOWN,UP,RIGHT,LEFT = 0,1,2,3
    # Here, a collection of all fences is added to the node. We only add a fence if there's NO neighbour (of the same plant])
    fences = set()
    for f in range(4):
        if not neighbors[f]:
            fences.add((i,j,f))

    A[(plant, patch)][(i, j)] = (1, fences)
    return A[(plant, patch)][(i, j)]

visited = [[False for _ in range(m)] for _ in range(n)]
A = {}
[count_perimeter(i, j, m, n, A, garden[i][j], garden, visited, -1) for j in range(n) for i in range(m)]

def calc_price(patches):
    # patches is a set of tuples that are part of a patch, they contain:
    # area, fences=[(i,j,d)] where i,j is location, d = fence direction
    # DOWN,UP,RIGHT,LEFT = 0,1,2,3
    area = 0
    # The following dict holds all sets of a certain direction, as long as they are connected, they form the same
    # fence, meaning i can just count if there's a predecessor (i-1,j) or (i,j-1), and if not, I'll count it as a new fence.
    # basically like this:
    # -- __ --_
    # ^  ^  ^ ^
    # 0  3  6 8
    # The borders at 0,3,6,8 do NOT have a predecessor.
    sides = {
        0: set(),
        1: set(),
        2: set(),
        3: set()
    }
    c = [0] * 4
    for t in patches:
        fences = t[1]
        area += t[0]
        for f in fences:
            # What I do here is: put the fences of each type (above, below, left, right) in each own set.
            # It allows me to ONLY check if a predecessor exists of this fence (meaning, an adjoining part of the same side)
            # could have also done an additional check on type, but I like the logic here
            sides[f[2]].add((f[0],f[1]))
    for k, side in sides.items():
        for l in side:
            # 0 is the bottom fence, 1 is the top: (as I noted before:     # DOWN,UP,RIGHT,LEFT = 0,1,2,3)
            # The only thing to make sure is to only count a single element of each connected component of the disjoint graph
            # So k == 0 / k == 1 means that there's a top/bottom fence and that means the left and right fence could be
            # part of the same fences, hence we have (i,j-1) for these
            if k == 0 or k == 1:
                c[k] +=  not (l[0],l[1]-1) in side
            # and similarly for 2, 3 they are right, left fences, so we check upwards
            if k == 2 or k == 3:
                c[k] += not (l[0]-1,l[1]) in side
    return sum(c)*area


plant_sums = 0
for plant_key, patch in A.items():
    plant_type = plant_key[0]
    patch_root = plant_key[1]

    plant_sums += calc_price(patch.values())

print(plant_sums)
