with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge1(val):
    val += val[0] # dont deal with wrap-around
    count = 0
    for pos in xrange(1, len(val)):
        if val[pos] == val[pos-1]:
            count += int(val[pos])
    return count

print solve_challenge1(INPUT)


def solve_challenge2(val):
    count = 0
    length = len(val)
    half = length//2
    for pos in xrange(0, length):
        if val[pos] == val[(pos+half) % length]:
            count += int(val[pos])
    return count

print solve_challenge2(INPUT)
