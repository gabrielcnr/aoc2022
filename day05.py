from collections import defaultdict
import re

from aoc import read_input


def part1(lines):
    stacks = defaultdict(list)
    for line in lines:
        if '[' in line:
            line = line.replace(' ' * 4, '[.] ').replace(' ', '').replace('][', '] [')
            crates = re.findall(r'\[(.)\]', line)
            for i, crate in enumerate(crates, 1):
                if crate != '.':
                    stacks[i].append(crate)

        elif line.startswith('move'):
            count, source, dest = [int(n) for n in re.findall(' (\d+)', line)]
            make_move(stacks, count, source, dest)

    print_stacks(stacks)
    print(sum(len(v) for v in stacks.values()))
    return stacks
    


def print_stacks(stacks):
    for k, v in sorted(stacks.items()):
        print(k, v)


#def make_move2(stacks, count, source, dest):
#    moved_crates = stacks[source][:count]
#    stacks[dest] = moved_crates[::-1] + stacks[dest]
#    stacks[source][:count] = []


def make_move(stacks, count, source, dest):
    if source == 4 or dest == 4:
        print(f'move {count} from {source} to {dest}')
        print('before', len(stacks[4]))
    for _ in range(count):
        stacks[dest].insert(0, stacks[source].pop(0))
    if source == 4 or dest == 4:        
        print('after', len(stacks[4]))
        print()


def test_make_move():
    stacks = {0: ['a', 'b', 'c'], 1: ['d', 'e']}
    make_move(stacks, 1, 1, 0)
    assert stacks == {0: ['d', 'a', 'b', 'c'], 1: ['e']}

    make_move(stacks, 1, 0, 1)
    assert stacks == {0: ['a', 'b', 'c'], 1: ['d', 'e']}

    make_move(stacks, 2, 0, 1)
    assert stacks == {0: ['c'], 1: ['b', 'a', 'd', 'e']}

    make_move(stacks, 2, 1, 0)
    assert stacks == {0: ['a', 'b', 'c'], 1: ['d', 'e']}


def test_part1():
    lines = read_input(test=True)
    stacks = part1(lines)
    assert [['C'], ['M'], ['Z', 'N', 'D', 'P']] == [v for k, v in sorted(stacks.items())]
    assert 'CMZ' == ''.join((v[0] for k, v in sorted(stacks.items())))


if __name__ == '__main__':
    lines = read_input()

    p1 = part1(lines)
    p1_text = ''.join((v[0] for k, v in sorted(p1.items())))
    print(f'Part 1: {p1_text}')
