
from functools import reduce


TEST_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def get_risk_level(input_str):
    data_list = input_str.splitlines()
    row_length = len(data_list)
    column_length = len(data_list[0])
    output = 0
    lowest_list = []
    for idx, data_str in enumerate(data_list):
        data_list[idx] = list(map(int, [chr for chr in data_str]))

    for row_idx, row in enumerate(data_list):
        for col_idx, value in enumerate(row):
            left_check = value < row[col_idx-1] if col_idx != 0 else True
            right_check = value < row[col_idx + 1] if col_idx != (column_length-1) else True
            top_check = value < data_list[row_idx - 1][col_idx] if row_idx != 0 else True
            bottom_check = value < data_list[row_idx + 1][col_idx] if row_idx != (row_length-1) else True
            if all([left_check, right_check, top_check, bottom_check]):
                lowest_list.append(value)

    for item in lowest_list:
        output += (item + 1)

    return output


def recursive_basin_height(depth_matrix, x, y, x_max, y_max):
    if (x == x_max) or (y == y_max) or x < 0 or y < 0 or depth_matrix[x][y][0] == 9 or depth_matrix[x][y][1]:
        return 0
    mark_visited = list(depth_matrix[x][y])
    mark_visited[1] = True
    depth_matrix[x][y] = mark_visited
    output = 1
    output += recursive_basin_height(depth_matrix, x - 1, y, x_max, y_max)
    output += recursive_basin_height(depth_matrix, x + 1, y, x_max, y_max)
    output += recursive_basin_height(depth_matrix, x, y - 1, x_max, y_max)
    output += recursive_basin_height(depth_matrix, x, y + 1, x_max, y_max)
    return output


def get_basins_output(input_str):
    data_list = input_str.splitlines()
    row_length = len(data_list)
    column_length = len(data_list[0])
    depth_matrix = []
    lowest_list = []
    basin_heights = []
    for x_idx, data_str in enumerate(data_list):
        row_array = []
        for y_idx in range(0, len(data_str)):
            row_array.append((int(data_str[y_idx]), False))
        depth_matrix.append(row_array)

    for row_idx, row in enumerate(data_list):
        for col_idx, value in enumerate(row):
            value = value[0]
            left_check = value < row[col_idx - 1] if col_idx != 0 else True
            right_check = value < row[col_idx + 1] if col_idx != (column_length - 1) else True
            top_check = value < data_list[row_idx - 1][col_idx] if row_idx != 0 else True
            bottom_check = value < data_list[row_idx + 1][col_idx] if row_idx != (row_length - 1) else True
            if all([left_check, right_check, top_check, bottom_check]):
                lowest_list.append((value, row_idx, col_idx))

    for each in lowest_list:
        basin_heights.append(recursive_basin_height(depth_matrix, each[1], each[2], row_length, column_length))
    basin_heights = sorted(basin_heights, reverse=True)
    print(basin_heights)
    return reduce(lambda x, y: x * y, basin_heights[:3])


# print(get_basins_output(TEST_DATA))
with open('input.in', 'r') as f:
    print(get_basins_output(f.read()))

