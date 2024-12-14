from time import sleep

bots = []
map_size = None

def update_positions(bots, time_delta, map_size):
    for bot in bots:
        bot['x'] = (bot['x'] + bot['vx'] * time_delta) % map_size[0]
        bot['y'] = (bot['y'] + bot['vy'] * time_delta) % map_size[1]

def bot_count_per_position(bots):
    pos = {}
    for i in bots:
        pos[(i['x'], i['y'])] = pos.get((i['x'], i['y']), 0) + 1
    return pos

def bot_count_per_position_quadrant(bots, map_size):
    quads = {}
    for i in bots:
        mid_x = map_size[0] // 2
        mid_y = map_size[1] // 2
        if i['x'] == mid_x or i['y'] == mid_y:
            continue
        quad = (i['x'] > mid_x, i['y'] < mid_y)
        quads[quad] = quads.get(quad, 0) + 1
    return quads

def display_grid(bots_map, map_size,elapsed):
    # let's only print something if there is a long line of bots, then validate visually
    bot_line_limit = map_size[0] - 70
    has_line_of_bots = any(
        sum((x, y) in bots_map for x in range(map_size[0])) >= bot_line_limit
        for y in range(map_size[1])
    )
    if not has_line_of_bots:
        return
    for y in range(map_size[1]):
        print()
        for x in range(map_size[0]):
            # I presume the three will look something like:
            #       1
            #      111
            #     11111
            #    1111111 < where this line is of significant width (maybe full width)
            #       1
            #      111
            char = "1" if (x, y) in bots_map else "0"
            print(char,end='')
    print("PRINTED  THIS AFTER %s ROUNDS", elapsed)

with open("inputs/14_1.txt") as file:
    for line in file:
        if not map_size:
            map_size = list(map(int, line.strip().split()))
            continue
        d = line.strip().split(" ")
        x, y = d[0].split("=")[1].split(",")
        vx, vy = d[1].split("=")[1].split(",")
        bots.append({
            'x': int(x),
            'y': int(y),
            'vx': int(vx),
            'vy': int(vy)
        })
# print(bot_count_per_position(bots))

safety_level = 1
for _, qs in bot_count_per_position_quadrant(bots,map_size).items():
    safety_level *= qs
print(safety_level)

elapsed=0
while True:
    update_positions(bots, 1, map_size)
    bots_map = bot_count_per_position(bots)
    # print(bots_map)
    display_grid(bots_map, map_size, elapsed)
    elapsed += 1
    # print()
    # print(elapsed)
    # sleep(1)




