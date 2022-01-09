
TEST_DATA = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def get_unmarked_points(input_str, first_op):
    impressions = []
    operations = []
    data_list = []
    column_length = 0
    row_length = 0
    dot_count = 0
    for data_str in input_str.splitlines():
        if data_str == '':
            continue
        elif 'fold along' in data_str:
            operations.append(data_str.split()[-1])
        else:
            x, y = data_str.split(',')
            x, y = int(x), int(y)
            impressions.append((x, y))
            if x > column_length:
                column_length = x
            if y > row_length:
                row_length = y

    row_length += 1
    column_length += 1
    for _ in range(0, row_length):
        data_list.append([0 for _ in range(column_length)])

    for impression in impressions:
        imp_x, imp_y = impression
        data_list[imp_y][imp_x] = 1

    for operation in operations:
        op = operation
        value = int(op.split('=')[1])
        if 'y=' in op:
            diff_value = 2
            for row_idx in range(value+1, row_length):
                for col_idx in range(column_length):
                    current_value = data_list[row_idx][col_idx]
                    to_be_updated_value = data_list[row_idx-diff_value][col_idx]
                    new_value = current_value + to_be_updated_value
                    if new_value > 1:
                        new_value = 1
                    data_list[row_idx - diff_value][col_idx] = new_value
                diff_value += 2
            row_length = value
        else:
            diff_value = 2
            for col_idx in range(value + 1, column_length):
                for row_idx in range(row_length):
                    current_value = data_list[row_idx][col_idx]
                    to_be_updated_value = data_list[row_idx][col_idx - diff_value]
                    new_value = current_value + to_be_updated_value
                    if new_value > 1:
                        new_value = 1
                    data_list[row_idx][col_idx - diff_value] = new_value
                diff_value += 2
            column_length = value
    for row_idx in range(row_length):
        output = ''
        for col_idx in range(column_length):
            value = data_list[row_idx][col_idx]
            output += '#' if value > 0 else '.'
            if value > 0:
                dot_count += 1
        # Output print is necessary to print the pattern that has 8 digit-code
        # In my case, the output translates to ZUJUAFHP
        # Blinking eyes fast enough helped see the pattern
        # ####.#..#...##.#..#..##..####.#..#.###..
        # ...  # .#..#....#.#..#.#..#.#....#..#.#..#.
        # ..  # ..#..#....#.#..#.#..#.###..####.#..#.
        # .  # ...#..#....#.#..#.####.#....#..#.###..
        # # ....#..#.#..#.#..#.#..#.#....#..#.#....
        # ####..##...##...##..#..#.#....#..#.#....
        print(output)

    return dot_count


# print(get_unmarked_points(TEST_DATA, first_op=True))
with open('input.in', 'r') as f:
    print(get_unmarked_points(f.read(), first_op=True))
