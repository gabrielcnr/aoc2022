import pytest


def make_moves(moves):
    head = (0, 0)
    tail = (0, 0)
    visited = {tail}
    for move in moves:
        direction, count = move.split()
        for _ in range(int(count)):
            head = move_head(head, direction)
            if not adjacent(head, tail):
                tail = move_tail(head, tail)
                visited.add(tail)
    return visited


deltas = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


def move_head(head, direction):
    x, y = head
    dx, dy = deltas[direction]
    return x + dx, y + dy


def adjacent(head, tail):
    xh, yh = head
    xt, yt = tail
    return abs(xh - xt) <= 1 and abs(yh - yt) <= 1


def move_tail(head, tail):
    xh, yh = head
    xt, yt = tail

    dx = abs(xh - xt)
    dy = abs(yh - yt)

    if (dx > 1 and dy > 0) or (dy > 1 and dx > 0):
        # move in diagonal
        if xh > xt:
            x = 1
        else:
            x = -1

        if yh > yt:
            y = 1
        else:
            y = -1

    else:
        if dx > dy:
            x = 1 if xh > xt else - 1
            y = 0
        else:
            x = 0
            y = 1 if yh > yt else -1

    return xt + x, yt + y


def test_adjacent():
    assert adjacent((2, 2), (3, 3))
    assert adjacent((8, 8), (8, 8))
    assert adjacent((5, 6), (5, 7))
    assert adjacent((2, 3), (3, 4))

    assert not adjacent((6, 4), (2, 9))
    assert not adjacent((2, 3), (2, 5))


@pytest.mark.parametrize(
    ['head', 'tail', 'new_tail'],
    [
        [(3, 0), (1, 0), (2, 0)],
        [(5, 2), (5, 4), (5, 3)],
        [(4, 6), (4, 2), (4, 3)],
        [(3, 6), (2, 4), (3, 5)],  # diagonal
    ]
)
def test_move_tail(head, tail, new_tail):
    assert new_tail == move_tail(head, tail)


TEST = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def part1(lines):
    visited = make_moves(lines)
    return len(visited)


def test_part1():
    lines = TEST.splitlines()
    assert 13 == part1(lines)


if __name__ == '__main__':
    from aoc import read_input

    lines = read_input()

    p1 = part1(lines)
    print(f'Part 1: {p1}')
