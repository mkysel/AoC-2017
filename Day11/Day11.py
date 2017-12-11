with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    # https://www.redblobgames.com/grids/hexagons/
    x = 0
    y = 0
    z = 0

    dists = []

    for d in val:
        if d == "n":
            y += 1
            z -= 1
        elif d == "s":
            y -= 1
            z += 1
        elif d == "ne":
            x += 1
            z -= 1
        elif d == "sw":
            x -= 1
            z += 1
        elif d == "nw":
            x -= 1
            y += 1
        elif d == "se":
            x += 1
            y -= 1
        dists.append((abs(x) + abs(y) + abs(z)) / 2)

    return dists[-1], max(dists)

print solve_challenge(INPUT.split(","))
