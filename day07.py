from functools import cached_property


class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def __iter__(self):
        return iter(self.children)

    @cached_property
    def size(self):
        return sum(c.size for c in self)

    def add(self, child):
        self.children.append(child)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size



lines = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()


def process_input(lines):
    root = Dir('/', None)
    curdir = None
    for line in lines:
        if line.startswith('$'):
            _, cmd, *args = line.split()
            if cmd == 'cd':
                dir, = args
                if dir == '/':
                    curdir = root
                elif dir == '..':
                    curdir = curdir.parent
                else:
                    curdir = next((x for x in curdir if x.name == dir), None)
                    assert curdir is not None
        else:
            dir_or_size, name = line.split()
            if name not in (child.name for child in curdir):
                if dir_or_size == 'dir':
                    child = Dir(name, parent=curdir)
                else:
                    child = File(name, int(dir_or_size))
                curdir.add(child)

    return root


def walkdirs(dir):
    yield dir
    for child in dir:
        if isinstance(child, Dir):
            yield from walkdirs(child)


def test_walkdirs():
    root = process_input(lines)

    expected = {"/": 48381165, "a": 94853, "e": 584, "d": 24933642}
    assert expected == {d.name: d.size for d in walkdirs(root)}


def test_dirs_and_files():
    a = Dir('a', None)
    b = Dir('b', parent=a)
    c = Dir('c', parent=a)
    d = Dir('d', parent=c)

    f1 = File('f1', 10)
    f2 = File('f2', 20)
    f3 = File('f3', 30)
    f4 = File('f4', 40)
    f5 = File('f5', 50)

    a.children = [b, c, f1]
    b.children = [f2, f3]
    c.children = [d, f4]
    d.children = [f5]

    assert 50 == d.size
    assert 90 == c.size
    assert 50 == b.size
    assert 150 == a.size


def part1(lines):
    root = process_input(lines)
    total = 0
    for dir in walkdirs(root):
        if (size := dir.size) <= 100000:
            total += size
    return total


def test_part1():
    assert 95437 == part1(lines)


if __name__ == '__main__':
    from aoc import read_input
    lines = read_input()
    p1 = part1(lines)
    print(f'Part 1: {p1}')
