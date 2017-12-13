SMALL_INPUT = '''0: 3
1: 2
4: 4
6: 4'''

with open("input.txt", "r") as f:
    INPUT = f.read()


def is_at_pos0(range_of_field, time):
    return time % ((range_of_field-1)*2) == 0


def get_severity(firewalls):
    total_severity = 0
    for time in xrange(max(firewalls.keys())+1):
        if firewalls.get(time):
            if is_at_pos0(firewalls[time], time):
                total_severity += (time*firewalls[time])

    return total_severity


def got_caught(firewalls, delay):
    for time in xrange(max(firewalls.keys())+1):
        if firewalls.get(time):
            if is_at_pos0(firewalls[time], time+delay):
                return True

    return False


def solve_challenge(val):
    firewalls = dict()
    for line in val:
        (key, range_of_field) = line.split(": ")
        firewalls[int(key)] = int(range_of_field)

    task1 = get_severity(firewalls)

    # naive solution
    delay = 10
    while got_caught(firewalls, delay):
        delay += 1

    return task1, delay

print solve_challenge(INPUT.split("\n"))
