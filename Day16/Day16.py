SMALL_INPUT = "s1,x3/4,pe/b"

with open("input.txt", "r") as f:
    INPUT = f.read()

def solve_challenge(val):
    #dancers = list("abcde")
    dancers = list("abcdefghijklmnop")

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

    return ''.join(dancers)

print solve_challenge(INPUT.split(","))
