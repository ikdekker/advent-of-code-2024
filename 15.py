walls = set()
boxes = set()
bot = (0, 0)
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # directions: U, R, D, L
dirs_chars = "^>v<"
warehouse_map = []
movements = []

with open("inputs/15.txt") as file:
    map_read = False
    for line in file:
        l = line.strip()
        if l == "":
            map_read = True
            continue
        if not map_read:
            warehouse_map.append(l)
        else:
            movements.append(l)

for y, row in enumerate(warehouse_map):
    for x, o in enumerate(row):
        if o == '#':
            walls.add((x, y))
        elif o == 'O':
            boxes.add((x, y))
        elif o == '@':
            bot = (x, y)


def move_or_push(boxes, walls, bot, movement, dirs):
    d = dirs_chars.index(movement)
    dx, dy = dirs[d]

    new_bot = (bot[0] + dx, bot[1] + dy)

    if new_bot in walls:
        return bot

    if new_bot in boxes:
        new_box = (new_bot[0] + dx, new_bot[1] + dy)
        while new_box in boxes:
            next_box = (new_box[0] + dx, new_box[1] + dy)
            if next_box in walls:
                return bot
            new_box = next_box

        if new_box not in walls:
            boxes.remove(new_bot)
            boxes.add(new_box)
            return new_bot
        return bot
    return new_bot


for movement_line in movements:
    for m in movement_line:
        bot = move_or_push(boxes, walls, bot, m, dirs)

# Print the final map
for y, row in enumerate(warehouse_map):
    row_output = []
    for x, char in enumerate(row):
        pos = (x, y)
        if pos == bot:
            row_output.append('@')
        elif pos in boxes:
            row_output.append('O')
        elif pos in walls:
            row_output.append('#')
        else:
            row_output.append('.')
    print(''.join(row_output))

def calculate_gps_coordinates(box):
    distance_from_top = box[1]
    distance_from_left = box[0]
    gps_coordinate = 100 * distance_from_top + distance_from_left
    return gps_coordinate

print(sum(calculate_gps_coordinates(box) for box in boxes))
