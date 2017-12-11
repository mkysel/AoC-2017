SMALL_INPUT='''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''

with open("input.txt", "r") as f:
    INPUT = f.read()

def parse_instructions(val):
    raw = val.split("\n")
    return map(lambda x: x.split(" "), raw)


def solve_challenge(val):

    register = dict()
    operators = dict()
    running_max = 0

    operators[">"] = lambda x, y: x > y
    operators[">="] = lambda x, y: x >= y
    operators["<"] = lambda x, y: x < y
    operators["<="] = lambda x, y: x <= y
    operators["=="] = lambda x, y: x == y
    operators["!="] = lambda x, y: x != y
    operators["inc"] = lambda x, y: x + y
    operators["dec"] = lambda x, y: x - y

    for i in parse_instructions(val):
        change_lhs = i[0]
        change_operator = i[1]
        change_rhs = int(i[2])
        condition_lhs = i[4]
        condition_operator = i[5]
        condition_rhs = int(i[6])

        var = register.get(condition_lhs, 0)

        if operators[condition_operator](var, condition_rhs):
            changed_var = register.get(change_lhs, 0)
            register[change_lhs] = operators[change_operator](changed_var, change_rhs)

        running_max = max(running_max, max(register.values()))

    return max(register.values()), running_max

print solve_challenge(INPUT)


