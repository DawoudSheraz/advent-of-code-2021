import math

TEST_DATA = 'target area: x=20..30, y=-10..-5'
PUZZLE_INPUT = 'target area: x=155..182, y=-117..-67'


def parse_input(input_str):
    coords = input_str.split(':')[1].split(',')
    coords = list(map(lambda x: x.strip(), coords))
    x = coords[0][2:]
    y = coords[1][2:]
    x = sorted(list(map(int, x.split('..'))))
    y = sorted(list(map(int, y.split('..'))))
    return x, y


def find_highest_y(initial_x, initial_y, x_range, y_range):
    """
    Given initial x and y velocities and target x and y range, find the max y.
    """
    x, y = 0, 0
    max_y = 0
    entered_area = False
    comparison_factor = 1 if initial_y >= 0 else -1

    while True:
        if (x_range[0] <= x <= x_range[1]) and (y_range[0] <= y <= y_range[1]):
            entered_area = True
            break
        if x > x_range[1] or (y < y_range[0]):
            break
        x = x + initial_x
        y = y + initial_y

        if initial_x != 0:
            initial_x -= 1
        initial_y -= 1
        if y > (max_y * comparison_factor):
            max_y = y * comparison_factor
    return max_y, entered_area


def solve(input_str):
    x_range, y_range = parse_input(input_str)
    max_list = []
    velocity_list = []

    # Loop from sqrt of x1 as small x values do not get in the area
    for x in range(int(math.sqrt(x_range[0])), x_range[1]+1):
        # y is started from 0 because projectile needs to attain a certain height before falling down
        for y in range(0, abs(y_range[0])+1):
            for value in [1, -1]:
                y = y * value
                output, hit_target = find_highest_y(x, y, x_range, y_range)

                if hit_target and (x, y) not in velocity_list:
                    max_list.append(output)
                    velocity_list.append((x, y))

    print("Part 1", max(max_list))
    print("Part 2", len(velocity_list))


solve(PUZZLE_INPUT)