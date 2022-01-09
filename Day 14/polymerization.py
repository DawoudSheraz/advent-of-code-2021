import math
from collections import Counter, defaultdict

TEST_DATA = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def get_difference(input_str, steps):
    data_list = input_str.splitlines()
    template = data_list[0]
    mapping = {}
    for idx in range(1, len(data_list)):
        if data_list[idx] == '':
            continue
        key, value = data_list[idx].split('->')
        mapping[key.strip()] = value.strip()

    for step in range(0, steps):
        print(step)
        new_template = ''
        for idx in range(0, len(template)-1):
            current, next = template[idx], template[idx+1]
            polymer = mapping.get(f'{current}{next}')
            if polymer:
                new_template += f"{current}{polymer}"
            else:
                new_template += f"{current}"
        new_template += f"{template[-1]}"
        template = new_template

    counter = Counter(template).most_common()
    return counter[0][1] - counter[-1][1]


def get_difference_part_2(input_str, steps):
    data_list = input_str.splitlines()
    pair_map = defaultdict(int)
    rules_mapping = {}
    template = data_list[0]
    for idx in range(0, len(template) - 1):
        pair_map[f"{template[idx]}{template[idx+1]}"] += 1
    for idx in range(2, len(data_list)):
        key, value = data_list[idx].split('->')
        rules_mapping[key.strip()] = value.strip()
    for step in range(steps):
        updated_map = pair_map.copy()
        for key, value in pair_map.items():
            value_to_add = rules_mapping[key]
            first_pair = f"{key[0]}{value_to_add}"
            second_pair = f"{value_to_add}{key[1]}"

            updated_map[first_pair] = (updated_map[first_pair] + value)
            updated_map[second_pair] = (updated_map[second_pair] + value)
            updated_map[key] -= value
        pair_map = updated_map

    counter = defaultdict(int)
    for key, value in pair_map.items():
        ch_1, ch_2 = key[0], key[1]
        counter[ch_1] += value
        counter[ch_2] += value
    counter = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
    # First and last item are not duplicated, so add them to counter before splitting in half
    counter[template[0]] += 1
    counter[template[-1]] += 1
    values = list(counter.values())
    return math.ceil((values[0] - values[-1])/2)


# print(get_difference_part_2(TEST_DATA, 40))

with open('input.in', 'r') as f:
    print(get_difference_part_2(f.read(), 40))
