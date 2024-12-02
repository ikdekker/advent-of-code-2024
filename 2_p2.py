def violated_level(diff):
    return not 1 <= diff <= 3

def solve_input():
    total = 0
    with open("inputs/2_success.txt", "r") as file:
        for line in file:
            nums = list(map(int, line.split()))

            violated_incr = violated_decr = used_dampener_incr = used_dampener_decr = skip_incr = skip_decr = False
            for i in range(1,len(nums)):
                diff_incr = nums[i] - nums[i-1-skip_incr]
                diff_decr = nums[i-1-skip_decr] - nums[i]
                skip_incr = skip_decr = False

                # incr...
                if violated_level(diff_incr):
                    violated_incr = True
                    if i < len(nums) - 1:
                        diff = nums[i+1] - nums[i-1]
                        fixed_by_diff = not violated_level(diff)

                        if not used_dampener_incr:
                            diff2 = nums[i+1] - nums[i]
                            diff2_bridge = nums[i] - nums[i-2]
                            # we need to bridge the gap between the one we skipped, for cases such as 1,2,8,9
                            # not applicable when it's the first element
                            fixed_by_diff2 = not violated_level(diff2) and (not violated_level(diff2_bridge) or i == 1)
                            skip_incr = fixed_by_diff
                            violated_incr = not fixed_by_diff and not fixed_by_diff2
                        used_dampener_incr = True
                    else:
                        violated_incr = used_dampener_incr
                # decr...
                if violated_level(diff_decr):
                    violated_decr = True
                    if i < len(nums) - 1:
                        diff = nums[i-1] - nums[i+1]
                        fixed_by_diff = not violated_level(diff)

                        if not used_dampener_decr:
                            diff2 = nums[i] - nums[i+1]
                            diff2_bridge = nums[i-2] - nums[i]
                            # we need to bridge the gap between the one we skipped, for cases such as 9,8,2,1
                            # not applicable when it's the first element
                            fixed_by_diff2 = not violated_level(diff2) and (not violated_level(diff2_bridge) or i == 1)
                            skip_decr = fixed_by_diff
                            violated_decr = not fixed_by_diff and not fixed_by_diff2
                        used_dampener_decr = True
                    else:
                        violated_decr = used_dampener_decr
            if not violated_incr or not violated_decr:
                total += 1
    print(total)

solve_input()
