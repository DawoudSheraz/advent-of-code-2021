

def get_increment_count(data_list):
	count = 0

	for index in range(0, len(data_list) -3):
		set_1 = data_list[index] + data_list[index+1] + data_list[index+2]
		set_2 = data_list[index+3] + data_list[index+1] + data_list[index+2]
		if set_2 > set_1:
			count += 1
	return count


input_data = open('day_1.in', 'r').readlines()

input_data = [int(data) for data in input_data]
print(get_increment_count(input_data))

