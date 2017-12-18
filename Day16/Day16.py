SMALL_INPUT = "s1,x3/4,pe/b"

with open("input.txt", "r") as f:
    INPUT = f.read()


def dance(dancers, val):

    for move in val:
        if move[0] == "s":
            steps = int(move[1:])
            dancers = (dancers[-steps:] + dancers[:-steps])

        elif move[0] == "p":
            left, right = move[1:].split("/")
            idx_l = dancers.index(left)
            idx_r = dancers.index(right)

            dancers[idx_l], dancers[idx_r] = dancers[idx_r], dancers[idx_l]

        else: # x
            left, right = move[1:].split("/")
            idx_l = (int(left)) % len(dancers)
            idx_r = (int(right)) % len(dancers)

            dancers[idx_l], dancers[idx_r] = dancers[idx_r], dancers[idx_l]

    return dancers


def solve_challenge(val):
    after_next = dance(list("abcdefghijklmnop"), val)
    task1 = ''.join(after_next)

    i = 1
    while i < 1000000000:
        after_next = dance(after_next, val)
        i += 1
        if after_next == list('abcdefghijklmnop'):
            i = 1000000000 - (1000000000 % i)

    task2 = ''.join(after_next)

    return task1, task2

print solve_challenge(INPUT.split(","))