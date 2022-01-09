import math

TEST_DATA = "16,1,2,0,4,2,7,1,2,14"


def get_fuel_part_2(data_str):
    fuel = 0
    data_list = list(map(int, data_str.split(',')))
    data_list = sorted(data_list)
    data_avg = math.floor(sum(data_list) / len(data_list))
    for item in data_list:
        diff = abs(item - data_avg)
        fuel += ((diff * (diff + 1))/2)
    return fuel


def get_fuel(data_str):
    fuel = 0
    data_list = list(map(int, data_str.split(',')))
    data_list = sorted(data_list)
    list_count = len(data_list)
    median = data_list[int(list_count/2)] \
        if list_count % 2 == 0 \
        else (data_list[int((list_count-1)/2)] + data_list[int((list_count+1)/2)])/2
    for item in data_list:
        fuel += abs(item - median)
    return fuel


# print(get_fuel_part_2(TEST_DATA))
with open('input.in', 'r') as f:
    print(get_fuel_part_2(f.read()))


