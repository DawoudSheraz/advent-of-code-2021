
from collections import defaultdict

TEST_DATA = """Player 1 starting position: 4
Player 2 starting position: 8"""

PART_1_INPUT = """Player 1 starting position: 1
Player 2 starting position: 5"""


class Universe:

    def __init__(self, player_1_pos, player_2_pos, player_1_score=0, player_2_score=0):
        self.players_dict = {
            '1': {'score': player_1_score, 'pos': player_1_pos},
            '2': {'score': player_2_score, 'pos': player_2_pos}
        }
        self.winner_determined = False
        self.winner = None

    def update_position(self, dice_value, player):
        new_pos = self.players_dict[player]['pos'] + dice_value
        while new_pos > 10:
            new_pos -= 10
        self.players_dict[player]['pos'] = new_pos
        self.players_dict[player]['score'] += new_pos

    def get_winner(self):
        return self.winner

    def check_for_winner(self):
        if self.players_dict['1']['score'] >= 21:
            self.winner_determined = True
            self.winner = '1'
        elif self.players_dict['2']['score'] >= 21:
            self.winner_determined = True
            self.winner = '2'
        return self.winner_determined


PLAYER_SEQUENCE = {
    '1': '2',
    '2': '1'
}

# 27 possibilities for part 2, map of how many times each total sum appears across 27 universes
"""
 Breakdown of dice values across 27 universes
 * 1
    * 1
      * 1 (3)
      * 2 (4)
      * 3 (5)
    * 2
      * 1 (4)
      * 2 (5)
      * 3 (6)
    * 3
      * 1 (5)
      * 2 (6)
      * 3 (7)
 * 2
    * 1
      * 1 (4)
      * 2 (5)
      * 3 (6)
    * 2
      * 1 (5)
      * 2 (6)
      * 3 (7)
    * 3
      * 1 (6)
      * 2 (7)
      * 3 (8)
 * 3
    * 1
      * 1 (5)
      * 2 (6)
      * 3 (7)
    * 2
      * 1 (6)
      * 2 (7)
      * 3 (8)
    * 3
      * 1 (7)
      * 2 (8)
      * 3 (9)
"""
DICE_VALUES_UNIVERSE_FREQUENCY = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}


def update_universe_count(universe, universe_count_dict, count):
    """
    Find a universe from universe_count_dict whose player's info match that of
    universe and add count if present. Otherwise, add new entry for universe.
    """
    present = False
    player_dict = universe.players_dict
    for existing_verse, value in universe_count_dict.items():
        existing_verse_player_dict = existing_verse.players_dict
        if (
                player_dict['1'] == existing_verse_player_dict['1']
        ) and (
            player_dict['2'] == existing_verse_player_dict['2']
        ):
            present = True
            universe_count_dict[existing_verse] = count + value
            break
    if not present:
        universe_count_dict[universe] = count


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


def play_dice_game_part_2(input_str):
    input_list = input_str.splitlines()
    universe = Universe(int(input_list[0][-1]), int(input_list[1][-1]))
    universe_count = defaultdict(int)
    universe_count[universe] = 1
    player_1_wins = 0
    player_2_wins = 0
    active_player = '1'

    while universe_count:
        updated_universes = defaultdict(int)
        for universe, count in universe_count.items():
            players_dict = universe.players_dict
            for dice_value, universes in DICE_VALUES_UNIVERSE_FREQUENCY.items():
                new_uni = Universe(
                    players_dict['1']['pos'],
                    players_dict['2']['pos'],
                    players_dict['1']['score'],
                    players_dict['2']['score']
                )
                new_uni.update_position(dice_value, active_player)
                if new_uni.check_for_winner():
                    if new_uni.get_winner() == '1':
                        player_1_wins += (count * universes)
                    elif new_uni.get_winner() == '2':
                        player_2_wins += (count * universes)
                else:
                    update_universe_count(new_uni, updated_universes, count * universes)

        universe_count = updated_universes
        active_player = PLAYER_SEQUENCE[active_player]
        print(player_1_wins, player_2_wins)

    return player_1_wins if player_1_wins > player_2_wins else player_2_wins


print("Part 1:", play_dice_game(PART_1_INPUT))
print("Part 2:", play_dice_game_part_2(PART_1_INPUT))
