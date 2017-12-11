SMALL_INPUT = "0 2 7 0"
INPUT = "14	0 15	12	11	11	3	5	1	6	8	4	9	1	8	4"

def solve_challenge1(val):
    count = 0
    configurations = set()
    configurations.add(tuple(val))
    sizeof = len(val)

    print val

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


        print val
        if tuple(val) in configurations:
            return count

        configurations.add(tuple(val))


print solve_challenge1(map(int, INPUT.split()))


def solve_challenge2(val):
    count = 0
    configurations = set()
    configurations.add(tuple(val))
    sizeof = len(val)
    expected_state = None
    cycle_size = 0

    print val


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
        print tpl

        if not expected_state:
            if tpl in configurations:
                print "Found TPL", tpl
                expected_state = tpl

            configurations.add(tpl)
        else:
            cycle_size += 1
            if tpl == expected_state:
                return cycle_size



print solve_challenge2(map(int, INPUT.split()))