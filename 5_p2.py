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
        middle = 0
        ordered = True

        for i, num in enumerate(nums):
            ordered = ordered and check_predecessors(num, i, preceeded_by, nums)

        while not ordered:
            ordered = True
            middle = 0
            for i in range(0, len(nums)):
                for pi in preceeded_by[nums[i]]:
                    if not pi in nums[:i] and pi in nums[i:]:
                        # there's a predecessor after a successor, move it back
                        for j in range(i, len(nums)):
                            n = nums[j]
                            if n == pi:
                                tmp = nums[j]
                                k = j
                                while k > i:
                                    nums[k] = nums[k - 1]
                                    k -= 1
                                nums[i] = tmp

            for i, num in enumerate(nums):
                ordered = ordered and check_predecessors(num, i, preceeded_by, nums)
            middle = nums[len(nums) // 2]
        mp += middle

print(mp)