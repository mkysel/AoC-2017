def solve_challenge(val):
    x = 0
    y = 0
    z = 0

    dists = []

    for d in val:
      if d == "n":
        y += 1
        z -= 1
      elif d == "s":
        y -= 1
        z += 1
      elif d == "ne":
        x += 1
        z -= 1
      elif d == "sw":
        x -= 1
        z += 1
      elif d == "nw":
        x -= 1
        y += 1
      elif d == "se":
        x += 1
        y -= 1
      dists.append((abs(x) + abs(y) + abs(z)) / 2)

    return (abs(x) + abs(y) + abs(z)) / 2, max(dists)


with open("day11.txt", "r") as f:
    print solve_challenge(f.read().split(","))