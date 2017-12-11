SMALL_INPUT = "3,4,1,5"

with open("input.txt", "r") as f:
    INPUT = f.read()


def solve_challenge(lengths, val=range(256), nr_rotations=64):
    pos = 0
    skip = 0
    size_of = len(val)
    for _ in xrange(nr_rotations):
        for l in lengths:
            mid = l//2
            for idx in xrange(mid):
                val[(pos+l-idx-1) % size_of], val[(pos+idx) % size_of] = val[(pos+idx) % size_of], val[(pos+l-idx-1) % size_of]

            pos = (pos + l + skip) % size_of
            skip += 1

    task1 = val[0] * val[1]

    #dense up
    hsh = ""

    for i in xrange(16):
        c = val[i*16+0]
        c ^= val[i*16+1]
        c ^= val[i*16+2]
        c ^= val[i*16+3]
        c ^= val[i*16+4]
        c ^= val[i*16+5]
        c ^= val[i*16+6]
        c ^= val[i*16+7]
        c ^= val[i*16+8]
        c ^= val[i*16+9]
        c ^= val[i*16+10]
        c ^= val[i*16+11]
        c ^= val[i*16+12]
        c ^= val[i*16+13]
        c ^= val[i*16+14]
        c ^= val[i*16+15]
        hsh += "%02x" % c

    return task1, hsh


# Task 1
print solve_challenge(map(int, INPUT.split(",")), nr_rotations=1)

# Task 2
print solve_challenge(map(ord, "")+[17, 31, 73, 47, 23])
print solve_challenge(map(ord, "AoC 2017")+[17, 31, 73, 47, 23])
print solve_challenge(map(ord, "1,2,3")+[17, 31, 73, 47, 23])
print solve_challenge(map(ord, "1,2,4")+[17, 31, 73, 47, 23])
print solve_challenge(map(ord, INPUT)+[17, 31, 73, 47, 23])
