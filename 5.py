def check_predecessors(p, i, preceeded_by, nums):
    if p in preceeded_by:
        return all([pi in nums[:i] or not pi in nums[i:] for pi in preceeded_by[p]])
    return True

mp = 0
solving = False
preceeded_by = {}
with open("inputs/5.txt") as file:
    for line in file:
        if line.strip() == '':
            solving = True
            continue
        if not solving:
            rule = line.strip().split("|")
            preceeded_by[int(rule[1])] = preceeded_by.get(int(rule[1]), []) + [int(rule[0])]
            continue

        nums = list(map(int, line.split(",")))
        middle = nums[len(nums)//2]
        for i, num in enumerate(nums):
            middle = check_predecessors(num, i, preceeded_by, nums) * middle
        mp += middle

print(mp)