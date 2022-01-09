
TEST_DATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

ROW_LENGTH = COLUMN_LENGTH = 10


def can_flash(flash_check, x, y, energy_level):
    return (y, x) not in flash_check and energy_level > 9


def increment_level(flash_check, data_list, x, y):
    if (y,x) not in flash_check:
        data_list[y][x] += 1


def start_flash(flash_check, data_list, x, y):
    flash_check[y, x] = True
    data_list[y][x] = 0
    flash_count = 1

    if (x-1) >= 0:  # TODO: have a master method for encapsulating these steps
        increment_level(flash_check, data_list, x-1, y)
        if can_flash(flash_check, x-1, y, data_list[y][x-1]):
            flash_count += start_flash(flash_check, data_list, x-1, y)
        if (y-1) >= 0:
            increment_level(flash_check, data_list, x - 1, y-1)
            if can_flash(flash_check, x - 1, y-1, data_list[y-1][x - 1]):
                flash_count += start_flash(flash_check, data_list, x - 1, y-1)
        if (y+1) < ROW_LENGTH:
            increment_level(flash_check, data_list, x - 1, y+1)
            if can_flash(flash_check, x - 1, y+1, data_list[y+1][x - 1]):
                flash_count += start_flash(flash_check, data_list, x - 1, y+1)

    if (x+1) < COLUMN_LENGTH:
        increment_level(flash_check, data_list, x + 1, y)
        if can_flash(flash_check, x+1, y, data_list[y][x+1]):
            flash_count += start_flash(flash_check, data_list, x+1, y)
        if (y-1) >= 0:
            increment_level(flash_check, data_list, x + 1, y-1)
            if can_flash(flash_check, x + 1, y-1, data_list[y-1][x + 1]):
                flash_count += start_flash(flash_check, data_list, x + 1, y-1)
        if (y+1) < ROW_LENGTH:
            increment_level(flash_check, data_list, x + 1, y+1)
            if can_flash(flash_check, x + 1, y+1, data_list[y+1][x + 1]):
                flash_count += start_flash(flash_check, data_list, x + 1, y+1)

    if (y - 1) >= 0:
        increment_level(flash_check, data_list, x, y-1)
        if can_flash(flash_check, x, y - 1, data_list[y - 1][x]):
            flash_count += start_flash(flash_check, data_list, x, y - 1)
    if (y + 1) < ROW_LENGTH:
        increment_level(flash_check, data_list, x, y + 1)
        if can_flash(flash_check, x, y + 1, data_list[y + 1][x]):
            flash_count += start_flash(flash_check, data_list, x, y + 1)

    return flash_count


def get_flash_count(input_str, steps):
    sync_flash_step = None
    loop_check = True
    flash_count = 0
    data_list = input_str.splitlines()
    for idx, data_str in enumerate(data_list):
        data_list[idx] = list(map(int, [chr for chr in data_str]))

    for step_count in range(0, steps):
        flash_check = {}

        # Increase energy level by 1
        for row_idx, row in enumerate(data_list):  # row_idx = y
            for col_idx in range(COLUMN_LENGTH):   # col_idx = x
                data_list[row_idx][col_idx] += 1

        for row_idx, row in enumerate(data_list):  # row_idx = y
            for col_idx in range(COLUMN_LENGTH):   # col_idx = x
                if can_flash(flash_check, col_idx, row_idx, data_list[row_idx][col_idx]):
                    flash_count += start_flash(flash_check, data_list, col_idx, row_idx)

        if not sync_flash_step:
            loop_check = True
            for row_idx in range(ROW_LENGTH):
                if not loop_check:
                    break
                sync_flash_step = step_count
                for col_idx in range(COLUMN_LENGTH):
                    if (row_idx, col_idx) not in flash_check:
                        sync_flash_step = None
                        loop_check = False

    return flash_count, sync_flash_step + 1


with open('input.in', 'r') as f:
    print(get_flash_count(f.read(), 500))

