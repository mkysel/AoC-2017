with open("input.txt", "r") as f:
    INPUT = f.read()

array_of_data = filter(lambda x: x, map(lambda x: map(int, x.split()), INPUT.split("\n")))


def solve_challenge1(val):
    count = 0
    for line in val:
        count += abs(min(line) - max(line))
    return count

print solve_challenge1(array_of_data)


def solve_challenge2(val):
    count = 0
    for ele in val:
        for i in xrange(0, len(ele)-1):
            for j in xrange(i+1, len(ele)):
                if ele[i] % ele[j] == 0:
                    count += ele[i] // ele[j]
                elif ele[j] % ele[i] == 0:
                    count += ele[j] // ele[i]

    return count

print solve_challenge2(array_of_data)


