from collections import defaultdict
import re

from aoc import read_input


def part1(lines):
    stacks = defaultdict(list)
    for line in lines:
        if '[' in line:
            line = line.replace(' ' * 3, '[.]').replace('][', '] [')
            crates = re.findall(r'\[(.)\]', line)
            for i, crate in enumerate(crates, 1):
                if crate != '.':
                    stacks[i].append(crate)

        elif line.startswith('move'):
            # print_stacks(stacks)
            # print(sum(len(v) for v in stacks.values()))
            # import pdb; pdb.set_trace()
            #print(sorted(stacks.items()), '\n')
            count, source, dest = [int(n) for n in re.findall(' (\d+)', line)]
            make_move(stacks, count, source, dest)

    print_stacks(stacks)
    print(sum(len(v) for v in stacks.values()))
    return ''.join((v[0] for k, v in sorted(stacks.items())))


def print_stacks(stacks):
    for k, v in sorted(stacks.items()):
        print(k, v)


def make_move(stacks, count, source, dest):
    moved_crates = stacks[source][:count]
    stacks[dest] = moved_crates[::-1] + stacks[dest]
    stacks[source][:count] = []


def test_make_move():
    stacks = {0: ['a', 'b', 'c'], 1: ['d', 'e']}
    make_move(stacks, 1, 1, 0)
    assert stacks == {0: ['d', 'a', 'b', 'c'], 1: ['e']}

    make_move(stacks, 3, 0, 1)
    assert stacks == {0: ['c'], 1: ['b', 'a', 'd', 'e']}

    make_move(stacks, 2, 0, 1)
    assert stacks == {0: [], 1: ['c', 'b', 'a', 'd', 'e']}

    make_move(stacks, 2, 1, 0)
    assert stacks == {0: ['b', 'c'], 1: ['a', 'd', 'e']}


def test_part1():
    lines = read_input(test=True)
    assert 'CMZ' == part1(lines)


if __name__ == '__main__':
    lines = read_input()

    p1 = part1(lines)
    print(f'Part 1: {p1}')
