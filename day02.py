from aoc import read_input

my_choices = 'XYZ'
their_choices = 'ABC'


def score1(theirs, mine):
    score = (my_index := my_choices.index(mine)) + 1
    if theirs == their_choices[my_index]:
        score += 3
    elif theirs != their_choices[(my_index+1)%3]:
        score += 6
    return score


def score2(theirs, outcome):
    their_index = their_choices.index(theirs)
    offset = my_choices.index(outcome) - 1
    my_choice = my_choices[(their_index + offset) % 3]
    score = 3 + (offset * 3) + my_choices.index(my_choice) + 1
    return score


if __name__ == '__main__':
    total = 0
    for line in (lines := read_input().splitlines()):
    # for line in (lines := ['A Y', 'B X', 'C Z']):
        if line := line.strip():
            theirs, mine = line.split()
            round_score = score1(theirs, mine)
            # print(f'{round_score = }')
            total += round_score
    print('Part 1', f'{total = }')

    total = 0
    for line in lines:
        theirs, mine = line.split()
        round_score = score2(theirs, mine)
        # print(f'{round_score = }')
        total += round_score
    print('Part 2', f'{total = }')
