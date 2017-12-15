from Day10.Day10 import calculate_knot_hash

SMALL_INPUT = "flqrgnkx"

with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    rows = []
    for row in xrange(128):
        c = "%s-%d" % (val, row)
        knot = calculate_knot_hash(c)
        bin_hash = bin(int(knot, 16))[2:].zfill(128)
        rows += [(row, j) for j, d in enumerate(bin_hash) if d == '1']

    task1 = len(rows)
    nr_groups = 0

    while rows:
        stack = [rows[0]]
        while stack:
            (x, y) = stack.pop()
            if (x, y) in rows:
                rows.remove((x, y))
                stack += [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        nr_groups += 1

    return task1, nr_groups


print solve_challenge(INPUT)
