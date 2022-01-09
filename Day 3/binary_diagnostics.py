
from collections import Counter


TEST_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def get_power_consumption_part_1(input_str):
    data_list = [''] * 12
    gamma_rate = ''
    epsilon = ''
    for item in input_str:
        for idx, bit in enumerate(item):
            data_list[idx] = f"{data_list[idx]}{bit}"

    for data in data_list:
        counter = Counter(data)
        gamma_rate += counter.most_common()[0][0]
        epsilon += counter.most_common()[-1][0]
    gamma_rate = int(gamma_rate, 2)
    epsilon = int(epsilon, 2)
    return gamma_rate * epsilon


def get_column_bit_counter(column, data_list, item_type):
    reduced_list = [data[column] for data in data_list]
    counter = Counter(reduced_list)
    common_list = counter.most_common()
    if len(common_list) == 1:
        most_common = least_common = common_list[0]
    else:
        most_common = common_list[0]
        least_common = common_list[1]

    if item_type == "oxygen":
        return "1" if (most_common[1] == least_common[1]) else most_common[0]
    else:
        return "0" if (most_common[1] == least_common[1]) else least_common[0]


def get_item_rating(input_str, item_type):
    data_lists = input_str.splitlines()
    columns = len(data_lists[0])
    for column in range(0, columns):
        common_bit = get_column_bit_counter(column, data_lists, item_type)
        filtered_list = [data_str for data_str in data_lists if data_str[column] == common_bit]
        data_lists = filtered_list
        if len(filtered_list) == 1:
            break

    return int(data_lists[0], 2)


def get_list_support_rating_part_2(input_str):
    oxygen_rating = get_item_rating(input_str, "oxygen")
    co2_rating = get_item_rating(input_str, "co2")
    print(oxygen_rating * co2_rating)


with open('input.in', 'r') as f:
    # data_list = f.readlines()
    # data_list = [item.strip() for item in data_list]
    print(get_list_support_rating_part_2(f.read()))
