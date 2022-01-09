
from collections import Counter, OrderedDict


TEST_DATA = "3,4,3,1,2"


def get_lanternfish_count(timer_list, days):
    """
    Trivial solution that just appends the new fishes to the end of list.
    """
    for count in range(0, days):
        elem_to_add = []
        for idx in range(0, len(timer_list)):
            timer_list[idx] -= 1
            if timer_list[idx] < 0:
                timer_list[idx] = 6
                elem_to_add.append(8)
        if elem_to_add:
            timer_list.extend(elem_to_add)
    return len(timer_list)


def get_lanternfish_count_v2(timer_list, days):
    """
    Dict based solution to use age as keys for counting the fishes.
    """
    output = 0
    fish_age_map = OrderedDict({idx: 0 for idx in range(9)})
    fish_age_counter = Counter(timer_list)
    fish_age_map.update(fish_age_counter.items())
    for count in range(0, days):
        new_fish_count = fish_age_map[0]
        for key in fish_age_map.keys():
            if key != 8 and key != 6:  # if age is neither 6 or 8, just shift age by -1 in terms of keys
                fish_age_map[key] = fish_age_map[key+1]
            elif key == 6:  # 6th age will get fishes from recent 0 and 7 age
                fish_age_map[key] = new_fish_count + fish_age_map[key+1]
        fish_age_map[8] = new_fish_count  # new first count is equal to index/key at 0

    for value in fish_age_map.values():
        output += value
    return output


def part_1(input_str, days):
    data_list = list(map(int, input_str.split(',')))
    return get_lanternfish_count(data_list, days)


def part_2(input_str, days):
    data_list = list(map(int, input_str.split(',')))
    return get_lanternfish_count_v2(data_list, days)


with open('input.in', 'r') as f:
    input_data = f.read()
    print(f"Part 1:{part_2(input_data, 80)}")
    print(f"Part 2:{part_2(input_data, 256)}")
