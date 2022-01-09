
from collections import defaultdict

TEST_DATA = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def get_change_factor(val_1, val_2):
    if val_1 > val_2:
        return -1
    if val_1 < val_2:
        return 1
    return 0


def get_intersection_points(input_str, straight_only):
    data = input_str.splitlines()
    lines_list = []
    points_map = defaultdict(int)
    for line_data in data:
        start, end = line_data.split('->')
        start = list(map(int, start.strip().split(',')))
        end = list(map(int, end.strip().split(',')))
        lines_list.append(
            ((start[0], start[1]), (end[0], end[1]))
        )
    if straight_only:
        lines_list = [
            list_item for list_item in lines_list if
            (list_item[0][0] == list_item[1][0] or list_item[0][1] == list_item[1][1])
        ]

    for line in lines_list:
        x1, y1 = line[0]
        x2, y2 = line[1]

        x_factor = get_change_factor(x1, x2)
        y_factor = get_change_factor(y1, y2)
        x = x1
        y = y1
        while x != (x2 + x_factor) or y != (y2 + y_factor):
            points_map[(x, y)] += 1
            if x != (x2 + x_factor):
                x = x + x_factor
            if y != (y2 + y_factor):
                y = y + y_factor

    return sum([1 for x in list(points_map.values()) if x > 1])


with open('input.in', 'r') as f:
    input_data = f.read()
    print("Part 1:", get_intersection_points(input_data, straight_only=True))
    print("Part 2:", get_intersection_points(input_data, straight_only=False))

