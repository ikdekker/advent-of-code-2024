memo = {}

with open("inputs/11_1.txt") as file:
    stones = []
    for line in file:
        cleaned_stones_lol = line.strip().split()
        stones.extend(cleaned_stones_lol)

def expand_stone(stone, blinks):
    if stone in memo and blinks in memo[stone]:
        return memo[stone][blinks]
    ex = 0
    if blinks == 1:
        ex += 2 - (len(stone) % 2)
    else:
        if stone == "0":
            ex = expand_stone("1", blinks - 1)
        elif len(stone) % 2 == 0:
            mid = len(stone) // 2
            ex = expand_stone(str(int(stone[:mid])), blinks - 1) + expand_stone(str(int(stone[mid:])), blinks - 1)
        else:
            new_stone = str(int(stone) * 2024)
            ex = expand_stone(new_stone, blinks - 1)

    if stone not in memo:
        memo[stone] = {}
    memo[stone][blinks] = ex

    return ex

NR_BLINKS = 75
print(sum(expand_stone(v, NR_BLINKS) for v in stones))
