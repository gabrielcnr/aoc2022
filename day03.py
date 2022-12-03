import string

from aoc import read_input

priorities = string.ascii_letters


def part1(lines):
    lines = [l.strip() for l in lines]
    sum_priorities = 0
    for rucksack in lines:
        mid = len(rucksack) // 2
        first, second = rucksack[:mid], rucksack[mid:]
        common, = set(first) & set(second)
        priority = priorities.index(common) + 1
        sum_priorities += priority
    return sum_priorities


def part2(lines):
    lines = [l.strip() for l in lines]
    sum_priorities = 0

    def iter_groups(it, n):
        while True:
            group = []
            for _ in range(n):
                try:
                    group.append(next(it))
                except StopIteration:
                    return
            yield group

    for g1, g2, g3 in iter_groups(iter(lines), 3):
        badge, = set(g1) & set(g2) & set(g3)
        priority = priorities.index(badge) + 1
        sum_priorities += priority

    return sum_priorities


def test_part1():
    assert 157 == part1(open('test03.txt').readlines())


def test_part2():
    assert 70 == part2(open('test03.txt').readlines())


if __name__ == '__main__':
    lines = read_input().splitlines()
    p1 = part1(lines)
    print(f'Part 1: {p1}')

    p2 = part2(lines)
    print(f'Part 2: {p2}')
