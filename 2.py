total = 0
with open("inputs/2.txt", "r") as file:
    for line in file:
        nums = list(map(int, line.split()))
        incrementing = nums[1] > nums[0]
        violated = False
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1] if incrementing else nums[i-1] - nums[i]
            if not 1 <= diff <= 3:
                violated = True
                break
        if not violated:
            total += 1
print(total)


