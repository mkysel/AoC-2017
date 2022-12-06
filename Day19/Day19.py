import sys, re

def solve_challenge(input):
    data = [[c if c != ' ' else 0 for c in x.strip('\n')] for x in input]

    dx, dy = 0, 1
    y = 0
    x = data[y].index('|')
    seen = []
    steps = 0
    while data[y][x]:
        seen.extend(re.findall('[A-Z]', data[y][x]))
        steps += 1
        if data[y][x] == '+':
            if dx:
                dx, dy = 0, 1 if data[y + 1][x] else -1
            else:
                dx, dy = 1 if data[y][x + 1] else -1, 0
        x += dx
        y += dy

    print(''.join(seen))
    print(steps)


if __name__ == '__main__':
    with open("input.txt", "r") as f:
        INPUT = f.readlines()
    solve_challenge(INPUT)