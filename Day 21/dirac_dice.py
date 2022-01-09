
TEST_DATA = """Player 1 starting position: 4
Player 2 starting position: 8"""

PART_1_INPUT = """Player 1 starting position: 1
Player 2 starting position: 5"""


PLAYER_SEQUENCE = {
    '1': '2',
    '2': '1'
}


def play_dice_game(input_str):
    input_list = input_str.splitlines()
    players_dict = {
        '1': {'score': 0, 'pos': int(input_list[0][-1])},
        '2': {'score': 0, 'pos': int(input_list[1][-1])}
    }
    dice_throws = 0
    dice_value = 0
    active_player = '1'

    while True:
        pos_value = 0
        for count in range(3):
            dice_value += 1
            if dice_value > 100:
                dice_value = 1
            pos_value += dice_value
            dice_throws += 1
        pos_value += players_dict[active_player]['pos']
        while pos_value > 10:
            pos_value -= 10
        players_dict[active_player]['pos'] = pos_value
        players_dict[active_player]['score'] += pos_value
        if players_dict[active_player]['score'] >= 1000:
            break
        active_player = PLAYER_SEQUENCE[active_player]
    return dice_throws * players_dict[PLAYER_SEQUENCE[active_player]]['score']


print(play_dice_game(PART_1_INPUT))
