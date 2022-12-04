from aoc import read_input


def part1(lines):
    count = 0
    for line in lines:
        range_1, range_2 = line.split(',')

        a1, a2 = range_1.split('-')
        b1, b2 = range_2.split('-')

        a1, a2, b1, b2 = [int(n) for n in [a1, a2, b1, b2]]

        if (a1 >= b1 and a2 <= b2) or (b1 >= a1 and b2 <= a2):
            print(f'{line = }')
            count += 1
    return count


def part2(lines):
    count = 0
    for line in lines:
        range_1, range_2 = line.split(',')

        a1, a2 = range_1.split('-')
        b1, b2 = range_2.split('-')

        a1, a2, b1, b2 = [int(n) for n in [a1, a2, b1, b2]]

        does_not_overlap = ((a1 > b2) or (b1 > a2))
        if not does_not_overlap:
            # if ((a1 <= b2) and (b1 <= a2)):
            print(f'{line = }')
            count += 1
    return count


def test_part1():
    assert 2 == part1(read_input(test=True))


def test_part2():
    assert 4 == part2(read_input(test=True))


if __name__ == '__main__':
    lines = read_input()
    p1 = part1(lines)
    print(f'Part 1: {p1}')

    p2 = part2(lines)
    print(f'Part 2: {p2}')
