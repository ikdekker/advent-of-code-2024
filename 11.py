# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

with open("inputs/11_1.txt") as file:
    for line in file:
        stones = list(line.strip().split())
    NR_BLINKS = 25
    for i in range(NR_BLINKS):
        new_stones = []
        for v in stones:
            if v == "0":
                new_stones.append("1")
            elif len(v) %2 == 0:
                new_stones.append(v[:len(v)//2])
                new_stones.append(str(int(v[len(v)//2:])))
            else:
                new_stones.append(str(int(v) * 2024))

        stones = new_stones
print(len(stones))

