
TEST_DATA = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


LENGTH_MAP = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def get_count_part_1(input_str):
    data_list = input_str.splitlines()
    output_value = 0
    for each in data_list:
        signals, output = each.split('|')
        signals = signals.strip().split(' ')
        output = output.strip().split(' ')
        signals = [''.join(sorted(x)) for x in signals]
        output = [''.join(sorted(x)) for x in output]
        for signal in signals:
            if len(signal) in [2, 3, 4, 7]:
                output_value += output.count(signal)

    print(output_value)


def find_and_update_map(signal_list, comparison_value, map_dict, diff_value, digit):
    """
    Helper method to compare digits of comparison value and signals in signal list.
    If the difference is equal to diff value, add a new map entry.
    """
    for signal in signal_list:
        if len(set(signal) - set(comparison_value)) == diff_value:
            map_dict[signal] = digit
            signal_list.pop(signal_list.index(signal))
            return signal


def get_decoded_signal_output(signals, output):
    """
    logic for getting the char -> value map
    * 1, 4, 7, 8 have unique lengths
    * 4 +7 -> 9 (1 off in 4+7)
    * 9 -> 2 (1 off from 9)
    * 2 -> 3(1 off)
    * 3 -> 5(only 5 remaining with 5 signal length)
    * 5 -> 6 (all 5 digits in 6)
    * 6 -> 0 (the last one)
    """
    map_dict = {}
    ret_val = ''
    four_plus_seven = ''
    recent_value = None
    unique_length_signals = [x for x in signals if len(x) in [2, 3, 4, 7]]

    for signal in unique_length_signals:
        signal_length = len(signal)
        if signal_length in [3, 4]:
            four_plus_seven += signal
        map_dict[signal] = LENGTH_MAP[signal_length]
        signals.pop(signals.index(signal))

    six_length_signals = [x for x in signals if len(x) == 6]
    five_length_signals = [x for x in signals if len(x) == 5]

    # Sequence of calls here is important, given the logic added in the docstrings.
    recent_value = find_and_update_map(
        six_length_signals, four_plus_seven, map_dict, 1, 9
    )
    recent_value = find_and_update_map(
        five_length_signals, recent_value, map_dict, 1, 2
    )
    find_and_update_map(
        five_length_signals, recent_value, map_dict, 1, 3
    )

    map_dict[five_length_signals[0]] = 5
    recent_value = five_length_signals[0]

    find_and_update_map(
        six_length_signals, recent_value, map_dict, 1, 6
    )

    map_dict[six_length_signals[0]] = 0

    for each in output:
        ret_val += str(map_dict[each])
    return int(ret_val)


def get_count_part_2(input_str):
    data_list = input_str.splitlines()
    output_value = 0
    for each in data_list:
        signals, output = each.split('|')
        signals = signals.strip().split(' ')
        output = output.strip().split(' ')
        signals = [''.join(sorted(x)) for x in signals]
        output = [''.join(sorted(x)) for x in output]
        output_value += get_decoded_signal_output(signals, output)

    print(output_value)


# get_count_part_2(TEST_DATA)
with open('input.in', 'r') as f:
    get_count_part_2(f.read())