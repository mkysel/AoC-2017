from collections import deque

SMALL_INPUT = "3"

with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    buffer = deque([0])
    searching_for = 50000000

    for next_val in xrange(1, searching_for + 1):
        buffer.rotate(-val)
        buffer.append(next_val)

    return buffer[(list(buffer).index(0)+1) % len(buffer)]

print solve_challenge(int(INPUT))
