SMALL_INPUT = '''0
3
0
1
-3'''

with open("input.txt", "r") as f:
    INPUT = f.read()
array_of_data = map(int, INPUT.split())


def solve_challenge1(val):
    cnt = 0
    current_idx = 0
    while True:
        cnt += 1
        next_idx = current_idx + val[current_idx]
        val[current_idx] += 1
        if next_idx < 0 or next_idx >= len(val):
            return cnt

        current_idx = next_idx

print solve_challenge1(array_of_data)


def solve_challenge2(val):
    cnt = 0
    current_idx = 0
    while True:
        cnt += 1
        offset = val[current_idx]
        next_idx = current_idx + offset
        if offset >= 3:
            val[current_idx] -= 1
        else:
            val[current_idx] += 1
        if next_idx < 0 or next_idx >= len(val):
            return cnt

        current_idx = next_idx

print solve_challenge2(array_of_data)