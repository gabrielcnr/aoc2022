from aoc import read_input


if __name__ == '__main__':
    input_ = read_input()

    elfs = []
    calories_items = []
    for line in input_.splitlines():
        if line := line.strip():
            calories_items.append(int(line))
        else:
            elfs.append(calories_items)
            calories_items = []

    total_calories = sorted(sum(calories) for calories in elfs)

    print('Part 1', total_calories[-1])
    print('Part 2', (top3 := total_calories[-3:]), sum(top3))

