SMALL_INPUT = "3"

with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    buffer = [0]
    current_position = 0

    for next_val in xrange(1, 2018):
        next_position = (current_position + val) % len(buffer)
        buffer = buffer[:next_position+1] + [next_val] + buffer[next_position+1:]
        current_position = next_position+1

    return buffer[current_position+1]

print solve_challenge(int(INPUT))