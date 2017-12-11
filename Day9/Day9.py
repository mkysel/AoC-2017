def solve_challenge(s):
    i = 0
    garbage = False
    garbage_chars = 0  # part 2
    result = 0
    depth = 0
    while i < len(s):
        if s[i] == "!":
            i += 1  # skip next
        elif garbage:
            if s[i] == ">":
                garbage = False
            else:
                garbage_chars += 1  # part 2
        elif s[i] == "{":
            depth += 1
            result += depth
        elif s[i] == "}":
            depth -= 1
        elif s[i] == "<":
            garbage = True
        i += 1

    return result, garbage_chars


print solve_challenge("{}")
print solve_challenge("{{{}}}")
print solve_challenge("{{},{}}")
print solve_challenge("{{{},{},{{}}}}")
print solve_challenge("{<a>,<a>,<a>,<a>}")
print solve_challenge("{{<ab>},{<ab>},{<ab>},{<ab>}}")
print solve_challenge("{{<!!>},{<!!>},{<!!>},{<!!>}}")
print solve_challenge("{{<a!>},{<a!>},{<a!>},{<ab>}}")

with file("input.txt") as f:
    print solve_challenge(f.read())
