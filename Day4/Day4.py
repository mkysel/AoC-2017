with open("input.txt", "r") as f:
    INPUT = f.read()
array_of_data = INPUT.split("\n")


def solve_challenge1(val):
    cnt = 0
    for passphrase in val:
        codes = passphrase.split(" ")
        if len(codes) == len(set(codes)):
            cnt += 1

    return cnt

print solve_challenge1(array_of_data)


def solve_challenge2(val):
    cnt = 0
    for passphrase in val:
        codes = map(lambda x: str(sorted(list(x))), passphrase.split(" "))
        if len(codes) == len(set(codes)):
            cnt += 1

    return cnt

print solve_challenge2(array_of_data)


