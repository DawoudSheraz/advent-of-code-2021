

TEST_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

SCORE_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETION_MAP = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

BRACKETS_MAP = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

OPENING_BRACKETS = ['(', '[', '{', '<']
CLOSING_BRACKETS = [')', ']', '}', '>']


def find_corruption_score(input_str):
    data_list = input_str.splitlines()
    stack = [[] for _ in range(len(data_list))]
    score = 0
    for idx, line in enumerate(data_list):
        for item in line:
            if item in OPENING_BRACKETS:
                stack[idx].append(item)
            elif item in CLOSING_BRACKETS:
                popped = stack[idx].pop()
                if BRACKETS_MAP[popped] != item:
                    score += SCORE_MAP[item]

    return score


def find_median_score(input_str):
    data_list = input_str.splitlines()
    stack = [[] for _ in range(len(data_list))]
    corrupt_indices = []
    scores_list = []
    for idx, line in enumerate(data_list):
        for item in line:
            if item in OPENING_BRACKETS:
                stack[idx].append(item)
            elif item in CLOSING_BRACKETS:
                popped = stack[idx].pop()
                if BRACKETS_MAP[popped] != item:
                    corrupt_indices.append(idx)

    for idx, item in enumerate(stack):
        if idx in corrupt_indices:
            continue
        score = 0
        for chr in item[::-1]:
            score = (score * 5) + (COMPLETION_MAP[BRACKETS_MAP[chr]])
        scores_list.append(score)
    return (sorted(scores_list))[int(len(scores_list)/2)]
    # return score


# print(find_median_score(TEST_DATA))
with open('input.in', 'r') as f:
    print(find_median_score(f.read()))
