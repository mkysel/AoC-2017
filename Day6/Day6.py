with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(val):
    count = 0
    configurations = set()
    configurations.add(tuple(val))
    sizeof = len(val)
    expected_state = None
    cycle_size = 0
    count_at_beginning_of_cycle = 0

    while True:
        count += 1
        # modify val
        (max_idx, max_val) = max(enumerate(val), key=lambda x: x[1])
        val[max_idx] = 0
        equal_parts = max_val//sizeof
        idx_of_part = max_val % sizeof

        for idx_raw in xrange(sizeof):
            idx = (idx_raw+max_idx+1) % sizeof
            val[idx] += equal_parts
            if idx_raw < idx_of_part:
                val[idx] += 1

        tpl = tuple(val)

        if not expected_state:
            if tpl in configurations:
                expected_state = tpl
                count_at_beginning_of_cycle = count

            configurations.add(tpl)
        else:
            cycle_size += 1
            if tpl == expected_state:
                return count_at_beginning_of_cycle, cycle_size


print solve_challenge(map(int, INPUT.split()))
