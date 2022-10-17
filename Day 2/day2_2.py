

VERTICAL_OPERATIONS = ['up', 'down']

def calculate_position(data_list):
	x,y, aim = 0,0,0

	for item in data_list:
		command, value = item.split()
		value = int(value)

		if command in VERTICAL_OPERATIONS:
			if command == 'up':
				aim -= value
			else:
				aim += value

		elif command == 'forward':
			x += value
			y += aim * value
	return x*y


input_data = open('day_2.in', 'r').readlines()
print(calculate_position(input_data))