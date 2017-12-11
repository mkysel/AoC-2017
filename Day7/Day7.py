import re

SMALL_INPUT = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)'''

with open("input.txt", "r") as f:
    INPUT = f.read()


class Element:
    def __init__(self, nm, we, dep):
        self.name = nm
        self.weight = we
        self.dependant_names = dep
        self.dependants = []
        self.parent = None

    def __str__(self):
        parent_name = "ROOT"
        if self.parent:
            parent_name = self.parent.name
        return "{0} ({1}) -> {2} <- {3}".format(self.name, self.weight, self.dependant_names, parent_name)

all_elements = dict()

for row in INPUT.split("\n"):
    parsed = row.split("->")
    dependants = []
    if len(parsed) == 2:
        dependants = map(lambda x: x.strip(), parsed[1].split(","))

    lhs = parsed[0].strip().split(" ")
    name = lhs[0]
    weight = int(re.findall(r'\d+', lhs[1])[0])
    e = Element(name, weight, dependants)
    all_elements[name] = e

for e in all_elements.itervalues():
    for d in e.dependant_names:
        dependant = all_elements.get(d)
        dependant.parent = e
        e.dependants.append(dependant)


def balance(ptr):
    weights = [balance(dep) for dep in ptr.dependants]
    my_weight = sum(weights) + ptr.weight

    s = set(weights)

    if s and len(s) != 1:
        mx = max(weights)
        mi = min(weights)
        diff = mx - mi
        my_weight -= diff

        for w in enumerate(weights):
            if w[1] == mx:
                dep = ptr.dependants[w[0]]

                print "%s is %d should be %d" % (dep.name, dep.weight, dep.weight-diff)
                dep.weight -= diff

    return my_weight


def solve_challenge(tree):
    root = None
    for ele in tree.itervalues():
        if not ele.parent:
            root = ele
            break

    print "Root:", root.name
    balance(root)

solve_challenge(all_elements)
