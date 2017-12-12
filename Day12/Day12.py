SMALL_INPUT = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''


with open("input.txt", "r") as f:
    INPUT = f.read()


def get_group(reachable, start_from):
    visited = set()
    visited.add(start_from)

    stack = reachable[start_from]

    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        for child in reachable[v]:
            if child not in visited:
                stack.append(child)

    return visited


def solve_challenge(val):
    reachable = dict()

    for line in val:
        (key, values) = line.split(" <-> ")
        key = int(key)
        values = map(int, values.split(","))
        reachable[key] = values

    remaining_keys = set(reachable.keys())

    initial_group = get_group(reachable, 0)
    remaining_keys -= initial_group

    task1 = len(initial_group)
    nr_groups = 1

    while remaining_keys:
        next_value = next(iter(remaining_keys))
        next_group = get_group(reachable, next_value)
        remaining_keys -= next_group
        nr_groups += 1

    return task1, nr_groups

print solve_challenge(INPUT.split("\n"))
