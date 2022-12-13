def build_forest(lines: list[str]) -> list[list[int]]:
    return [[int(n) for n in line] for line in lines]


def count_visibles(forest: list[list[int]]) -> int:
    count = 0
    for i, trees in enumerate(forest):
        for j, height in enumerate(trees):
            if is_visible(i, j, forest):
                count += 1
    return count


def is_visible(i: int, j: int, forest: list[list[int]]):
    if i == 0 or j == 0 or i == len(forest) - 1 or j == len(forest[0]) - 1:
        return True

    height = forest[i][j]

    # TODO: refactor this and make it more efficient - once it's visible, it's visible!
    # left
    left = True
    for i2 in range(i - 1, -1, -1):
        if forest[i2][j] >= height:
            left = False
            break

    # right
    right = True
    for i2 in range(i + 1, len(forest[0])):
        if forest[i2][j] >= height:
            right = False
            break

    # up
    up = True
    for j2 in range(j - 1, -1, -1):
        if forest[i][j2] >= height:
            up = False
            break

    # down
    down = True
    for j2 in range(j + 1, len(forest)):
        if forest[i][j2] >= height:
            down = False
            break

    return any((left, right, up, down))


TEST = """\
30373
25512
65332
33549
35390\
"""


def test_count_visibles():
    forest = build_forest(TEST.splitlines())
    assert 21 == count_visibles(forest)


def part1(lines):
    forest = build_forest(lines)
    return count_visibles(forest)


if __name__ == '__main__':
   from aoc import read_input
   lines = read_input()

   p1 = part1(lines)
   print(f'Part 1: {p1}')