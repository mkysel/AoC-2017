with open("input.txt", "r") as f:
    INPUT = f.read()

SMALL_INPUT = "65\n8921"


def solve_challenge(val):
    factor_a = 16807
    factor_b = 48271
    mods = 2147483647
    nr_iterations = 5000000

    nr_matches = 0
    val_A, val_B = val

    for _ in xrange(nr_iterations):
        while True:
            val_A = (val_A * factor_a) % mods
            if val_A % 4 == 0:
                break

        while True:
            val_B = (val_B * factor_b) % mods
            if val_B % 8 == 0:
                break

        if val_A & 0xFFFF == val_B & 0xFFFF:
            nr_matches += 1

    return nr_matches

print solve_challenge(map(int, INPUT.split("\n")))
