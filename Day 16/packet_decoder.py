
from functools import reduce
TEST_DATA = 'D2FE28'

HEX_MAP = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def get_binary_representation(hex_string):
    output = ''
    for char in hex_string:
        output += HEX_MAP[char]
    return output


def parse_packet(packet_string, counter_position, packets_count=None):
    counter = counter_position
    try:
        version = int(packet_string[counter: counter + 3], 2)
        packet_type = int(packet_string[counter + 3: counter + 6], 2)
    except:
        return 0

    if len(packet_string) - counter <= 7:
        return 0

    if packets_count:
        packets_count -=1
        if packets_count  < 0:
            return 0

    counter += 6
    if packet_type == 4:
        print('literal value')
        decimal = ''

        while True:
            number = packet_string[counter: counter+5]
            decimal += number[1:]
            counter += 5
            if number[0] == '0':
                break

    else:
        id = packet_string[counter]
        if id == '0':
            sub_packets_length = int(packet_string[counter+1: counter+16], 2)
            counter += 16
            # packet_string_updated = packet_string[:counter + sub_packets_length + 1]
            output = version + parse_packet(packet_string, counter, packets_count)
            return output
        else:
            packet_count = int(packet_string[counter + 1: counter + 12], 2)
            counter += 12
            update_count = packets_count if packets_count else 0
            return version + parse_packet(packet_string, counter, packet_count + update_count)

    return version + parse_packet(packet_string, counter, packets_count)


def parse_packet_part_2(packet_string, counter_position):
    counter = counter_position
    try:
        packet_type = int(packet_string[counter + 3: counter + 6], 2)
    except:
        return None, None

    counter += 6

    if packet_type == 4:
        decimal = ''
        while True:
            number = packet_string[counter: counter+5]
            decimal += number[1:]
            counter += 5
            if number[0] == '0':
                return int(decimal, 2), counter

    else:
        packet_values = []
        id = packet_string[counter]
        if id == '0':
            sub_packets_length = int(packet_string[counter+1: counter+16], 2)
            counter += 16
            subpackets = packet_string[counter: counter + sub_packets_length]
            sub_counter = 0
            while sub_counter <= sub_packets_length:
                value, new_counter = parse_packet_part_2(subpackets, sub_counter)
                packet_values.append(value)
                if new_counter:
                    sub_counter = new_counter
                else:
                    break
            counter += sub_packets_length

        else:
            packet_count = int(packet_string[counter + 1: counter + 12], 2)
            counter += 12

            for _ in range(packet_count):
                value, new_counter = parse_packet_part_2(packet_string, counter)
                packet_values.append(value)
                if new_counter:
                    counter = new_counter

        packet_values = [x for x in packet_values if x is not None]
        if packet_type == 0:
            return reduce(lambda x, y: x+y, packet_values), counter
        elif packet_type == 1:
            return reduce(lambda x, y: x*y, packet_values), counter
        elif packet_type == 2:
            return min(packet_values), counter
        elif packet_type == 3:
            return max(packet_values), counter
        elif packet_type == 5:
            return 1 if packet_values[0] > packet_values[1] else 0, counter
        elif packet_type == 6:
            return 1 if packet_values[0] < packet_values[1] else 0, counter
        elif packet_type == 7:
            return 1 if packet_values[0] == packet_values[1] else 0, counter


def part_1(input_str):
    binary = get_binary_representation(input_str)
    print(len(binary))
    print(parse_packet(binary, 0))


def part_2(input_str):
    binary = get_binary_representation(input_str)
    print(binary)
    print(parse_packet_part_2(binary, 0))


# print(part_2('880086C3E88112'))
with open('input.in', 'r') as f:
    print(part_2(f.read()))
