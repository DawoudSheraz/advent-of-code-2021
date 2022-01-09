
def calculate_increases(data_list):
    count = 0
    for index in range(len(data_list) -1):
        if data_list[index] < data_list[index+1]:
            count += 1
    return count


input_data = open('sonar_sweep.in', 'r').readlines()
data = [int(data_item.strip()) for data_item in input_data if data_item.strip() != '']
print(calculate_increases(data))
