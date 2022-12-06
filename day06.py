from collections import deque


def find_marker(datastream: str):
    q = deque(maxlen=4)
    for i, c in enumerate(datastream, 1):
        q.append(c)
        if len(set(q)) == 4:
            return i


def test_part_1():
    assert 7 == find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    assert 5 == find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz')
    assert 6 == find_marker('nppdvjthqldpwncqszvftbrmjlhg')
    assert 10 == find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
    assert 11 == find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')


if __name__ == '__main__':
    from aoc import read_input

    p1 = find_marker(read_input()[0])
    print(f'Part 1: {p1}')

