from collections import defaultdict

SMALL_INPUT = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''

with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    idx = 0
    registry = defaultdict(int)
    send = None

    while True:
        if val[idx][0] == "set":
            try:
                registry[val[idx][1]] = int(val[idx][2])
            except ValueError:
                registry[val[idx][1]] = registry[val[idx][2]]
        elif val[idx][0] == "add":
            try:
                registry[val[idx][1]] += int(val[idx][2])
            except ValueError:
                registry[val[idx][1]] += registry[val[idx][2]]
        elif val[idx][0] == "mul":
            try:
                registry[val[idx][1]] *= int(val[idx][2])
            except ValueError:
                registry[val[idx][1]] *= registry[val[idx][2]]
        elif val[idx][0] == "mod":
            try:
                registry[val[idx][1]] %= int(val[idx][2])
            except ValueError:
                registry[val[idx][1]] %= registry[val[idx][2]]
        elif val[idx][0] == "snd":
            send = registry[val[idx][1]]
        elif val[idx][0] == "rcv":
            if registry[val[idx][1]] != 0:
                return send
        elif val[idx][0] == "jgz":
            if registry[val[idx][1]] > 0:
                    idx += int(val[idx][2])
                    continue
        idx += 1

print solve_challenge(map(lambda x: x.split(" "), INPUT.split("\n")))
