from time import sleep

walls = set()
boxes = set()
boxes_wide = set()
bot = (0, 0)
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # directions: U, R, D, L
dirs_txt = ["UP", "RIGHT", "DOWN", "LEFT"]  # directions: U, R, D, L
dirs_chars = "^>v<"
warehouse_map = []
movements = []

with open("inputs/15_1.txt") as file:
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


def print_wh_entry(pos,bot,boxes,boxes_wide, walls, emoji):
    if pos == bot:
        return "🤖" if emoji else '@'
    elif pos in boxes:
        return '📦📦' if emoji else '['
    elif pos in boxes_wide:
        return '' if emoji else ']'
    elif pos in walls:
        return '🧱' if emoji else '#'
    return "🟩" if emoji else '.'

def print_wh(warehouse_map, boxes, walls, bot):
    for y, row in enumerate(warehouse_map):
        row_output = []
        for x, char in enumerate(row):
            pos = (x * 2, y)
            use_emoji = len(warehouse_map[0]) < 40
            c = print_wh_entry(pos,bot,boxes,boxes_wide, walls, use_emoji)
            row_output.append(c)
            pos = (x * 2 + 1, y)
            c = print_wh_entry(pos,bot,boxes,boxes_wide, walls, use_emoji)
            row_output.append(c)
        print(''.join(row_output))

for y, row in enumerate(warehouse_map):
    for x, o in enumerate(row):
        if o == '#':
            walls.add((x * 2, y))
            walls.add((x * 2 + 1, y))
        elif o == 'O':
            boxes.add((x * 2, y))
            boxes_wide.add((x * 2 + 1, y))
        elif o == '@':
            bot = (x * 2, y)

def get_collided_box(pos, boxes, boxes_wide, dx):
    if pos in boxes and not dx == -1:
        return pos
    if pos in boxes_wide and not dx == 1:
        return pos[0] - 1, pos[1]
    return None

def update_positions(boxes, boxes_wide, walls, bot, dir):
    dx, dy = dir
    current_move = (bot[0] + dx, bot[1] + dy)
    box_queue = [get_collided_box(current_move, boxes, boxes_wide, 0)]
    affected = {}

    while len(box_queue) >= 1:
        current_move = box_queue.pop(0)
        current_move_wide = (current_move[0] + 1, current_move[1])
        if current_move in walls or current_move_wide in walls:
            return False

        collided_box = get_collided_box(current_move, boxes, boxes_wide, dx)
        collided_box_wide = get_collided_box(current_move_wide, boxes, boxes_wide, dx)

        if collided_box:
            affected[collided_box] = True
            push_target = (collided_box[0] + dx, collided_box[1] + dy)
            box_queue.append(push_target)

        if (collided_box and collided_box_wide and not collided_box[0] + 1 == collided_box_wide[0]) or (not collided_box and collided_box_wide):
            affected[collided_box_wide] = True
            push_target_wide = (collided_box_wide[0] + dx, collided_box_wide[1] + dy)
            box_queue.append(push_target_wide)

    alist = reversed(list(affected))
    for box in alist:
        boxes.add((box[0] + dx, box[1] + dy))
        boxes_wide.add((box[0] + dx + 1, box[1] + dy))
        boxes.remove(box)
        boxes_wide.remove((box[0] + 1, box[1]))

    return True

def move_or_push(boxes, boxes_wide, walls, bot, movement, dirs):
    d = dirs_chars.index(movement)
    dx, dy = dirs[d]

    new_bot = (bot[0] + dx, bot[1] + dy)

    if new_bot in walls:
        return bot

    if new_bot not in boxes and new_bot not in boxes_wide:
        return new_bot

    moved = update_positions(boxes, boxes_wide, walls, bot, dirs[d])
    return new_bot if moved else bot

print_wh(warehouse_map, boxes, walls, bot)

def calculate_gps_coordinates(box):
    distance_from_top = box[1]
    distance_from_left = box[0]
    gps_coordinate = 100 * distance_from_top + distance_from_left
    return gps_coordinate

mc=0
visualize = False
for movement_line in movements:
    for m in movement_line:
        bot = move_or_push(boxes, boxes_wide, walls, bot, m, dirs)
        if visualize:
            print("NEXT: " + dirs_txt[dirs_chars.index(m)] + " SUM: " + str(
                sum(calculate_gps_coordinates(box) for box in boxes)))
            print_wh(warehouse_map, boxes, walls, bot)
            sleep(0.0)
        mc+=1
print(sum(calculate_gps_coordinates(box) for box in boxes))
