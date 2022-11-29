def make_day(day: int) -> None:
    for ext in {'py', 'txt'}:
        fname = f'day{day:02d}.{ext}'
        open(fname, 'w')
        print(f'Wrote: {fname}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} [day_number]')
        sys.exit(1)
    make_day(int(sys.argv[1]))
