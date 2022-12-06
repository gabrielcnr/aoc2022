from collections import deque


def find_marker(datastream: str, count: int) -> int | None:
    q = deque(maxlen=count)
    for i, c in enumerate(datastream, 1):
        q.append(c)
        if len(set(q)) == count:
            return i


def test_part_1():
    assert 7 == find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4)
    assert 5 == find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 4)
    assert 6 == find_marker('nppdvjthqldpwncqszvftbrmjlhg', 4)
    assert 10 == find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 4)
    assert 11 == find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 4)


def test_part_2():
    assert 19 == find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
    assert 23 == find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14)
    assert 23 == find_marker('nppdvjthqldpwncqszvftbrmjlhg', 14)
    assert 29 == find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14)
    assert 26 == find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14)


if __name__ == '__main__':
    from aoc import read_input

    datastream = read_input()[0]

    p1 = find_marker(datastream, 4)
    print(f'Part 1: {p1}')

    p2 = find_marker(datastream, 14)
    print(f'Part 2: {p2}')
