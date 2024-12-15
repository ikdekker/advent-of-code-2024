import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def violated_level(diff):
    return not 1 <= diff <= 3

def create_single_animation(all_nums, success_list):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 8)

    scatter, = ax.plot([], [], 'bo', markersize=8)
    line, = ax.plot([], [], 'r-', lw=2)
    success_text = ax.text(0.5, 0.95, '', ha='center', va='top', transform=ax.transAxes, fontsize=12, color='green')

    def init():
        scatter.set_data([], [])
        line.set_data([], [])
        success_text.set_text('')
        return scatter, line, success_text

    def update(frame):
        current_frame = frame
        set_idx = 0

        # Find which set and which point in the set we are at
        while current_frame >= len(all_nums[set_idx]):
            current_frame -= len(all_nums[set_idx])
            set_idx += 1

        point_idx = current_frame

        # Update scatter plot
        x_data = np.arange(point_idx + 1)
        y_data = all_nums[set_idx][:point_idx + 1]
        scatter.set_data(x_data, y_data)

        # Dynamically update y-axis to fit the data
        ax.set_ylim(min(y_data) - 1, max(y_data) + 1)

        # Show success or failure message
        if success_list[set_idx]:
            success_text.set_text("Success!")
            # For success, draw the full line in green
            line.set_color('green')
            line.set_data(x_data, y_data)
        else:
            success_text.set_text("Failure: Element Removed")

            # Clear previous red line
            line.set_color('red')
            line.set_data([], [])  # Clear the red line before plotting new violations

            # Calculate the differences and plot in red for failure
            x_red = []
            y_red = []
            violation_show_in_frame = 0

            for i in range(1, len(all_nums[set_idx])):
                diff = all_nums[set_idx][i] - all_nums[set_idx][i - 1]
                violation_show_in_frame += 1
                if violation_show_in_frame > current_frame:
                    break
                if violated_level(diff):  # If difference is outside the valid range
                    x_red.append(i - 1)
                    x_red.append(i)
                    y_red.append(all_nums[set_idx][i - 1])
                    y_red.append(all_nums[set_idx][i])

            # Plot the red line for violations
            if x_red:
                line.set_color('red')
                line.set_data(x_red, y_red)  # Only plot the red line for violated points

        return scatter, line, success_text

    # Total number of frames is the sum of all the points in all the sets
    total_frames = sum(len(nums) for nums in all_nums)
    ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=100)

    plt.show()

def solve_input():
    total = 0
    all_nums = []
    success_list = []

    with open("../inputs/2.txt", "r") as file:
        for line in file:
            nums = list(map(int, line.split()))
            violated_incr = violated_decr = used_dampener_incr = used_dampener_decr = skip_incr = skip_decr = False

            for i in range(1, len(nums)):
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
                            fixed_by_diff2 = not violated_level(diff2) and (not violated_level(diff2_bridge) or i == 1)
                            skip_decr = fixed_by_diff
                            violated_decr = not fixed_by_diff and not fixed_by_diff2
                        used_dampener_decr = True
                    else:
                        violated_decr = used_dampener_decr

            if not violated_incr or not violated_decr:
                # Success: If no violation after applying dampener, add nums to the list
                all_nums.append(nums)
                success_list.append(True)
                total += 1
            else:
                nums.pop()
                all_nums.append(nums)
                success_list.append(False)

    # Create a single animation for all sets of nums
    create_single_animation(all_nums, success_list)

    print(f"Total Successes: {total}")

solve_input()
