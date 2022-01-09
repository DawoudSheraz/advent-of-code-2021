
TEST_DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


class BoardItem:

    def __init__(self, value):
        self.value = int(value)
        self.is_checked = False

    def mark_number(self):
        self.is_checked = True

    def __str__(self):
        return f"{self.value}-{self.is_checked}"


class Board:

    BOARD_SIZE = 5

    def __init__(self, data_str):
        self.board_items = []
        self.bingo_complete = False
        for data in data_str.splitlines():
            if data:
                self.board_items.append([BoardItem(value) for value in data.split() if value])

    def print_board(self):
        for row in self.board_items:
            for item in row:
                print(item)

    def mark_number(self, value):
        for row in self.board_items:
            for item in row:
                if item.value == value:
                    item.mark_number()

    def is_row_bingo(self):
        valid = False
        for row in self.board_items:
            checked = [item for item in row if item.is_checked]
            if len(checked) == self.BOARD_SIZE:
                valid = True
                self.bingo_complete = True
                print("row bingo")
                break
        return valid

    def is_column_bingo(self):
        valid = False
        for column in range(self.BOARD_SIZE):
            reduced_list = [data[column] for data in self.board_items]
            checked = [item for item in reduced_list if item.is_checked]
            if len(checked) == self.BOARD_SIZE:
                valid = True
                self.bingo_complete = True
                print("column bingo")
                break
        return valid

    def is_bingo(self):
        return self.is_row_bingo() or self.is_column_bingo()

    def get_score(self):
        unchecked = 0
        for idx, row in enumerate(self.board_items):
            for item in row:
                if not item.is_checked:
                    unchecked += item.value
        return unchecked


def part_1(bingo_input, boards):
    output = []
    for value in bingo_input.split(','):
        if output:
            break
        value = int(value)
        for idx, board in enumerate(boards):
            board.mark_number(value)
            if board.is_bingo():
                print(f"Board Number {idx}")
                output = board.get_score() * value
                break
    return output


def part_2(bingo_input, boards):
    output = None
    marked_boards = []
    for value in bingo_input.split(','):
        if output:
            break
        value = int(value)
        for idx, board in enumerate(boards):
            board.mark_number(value)
            if not board.bingo_complete and board.is_bingo():
                print(f"Board Number {idx}")
                marked_boards.append(board)
                if len(marked_boards) == len(boards):
                    output = marked_boards[-1].get_score() * value
    return output


def lets_bingo(input_str, part=1):
    text = input_str.splitlines()
    bingo_input = text[0]
    boards_list = []
    for count in range(2, len(text), 6):
        board_data_str = '\n'.join(text[count: count+5])
        boards_list.append(Board(board_data_str))

    if part == 1:
        return part_1(bingo_input, boards_list)
    elif part == 2:
        return part_2(bingo_input, boards_list)


with open('input.in', 'r') as f:
    print(lets_bingo(f.read(), 2))
