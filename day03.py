import string

from aoc import read_input

priorities = string.ascii_letters

def part1(lines):
    sum_priorities = 0
    for rucksack in lines:
        mid = len(rucksack) // 2
        first, second = rucksack[:mid], rucksack[mid:]
        common, = set(first) & set(second)
        priority = priorities.index(common) + 1
        sum_priorities += priority
    return sum_priorities


def test_part1():
    assert 157 == part1(open('test03.txt').readlines())


if __name__ == '__main__':
    lines = read_input().splitlines()
    p1 = part1(lines)
    print(f'Part 1: {p1}')