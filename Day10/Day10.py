SMALL_INPUT = "3,4,1,5"
INPUT = "63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24"


def solve_challenge1(val, lengths):
    pos = 0
    skip = 0
    size_of = len(val)
    for l in lengths:
        mid = l//2
        for idx in xrange(mid):
            val[(pos+l-idx-1) % size_of], val[(pos+idx) % size_of] = val[(pos+idx) % size_of], val[(pos+l-idx-1) % size_of]

        pos = (pos + l + skip) % size_of
        skip += 1

    return val

rotated = solve_challenge1(range(256), map(int, INPUT.split(",")))
print rotated[0] * rotated[1]

def solve_challenge2(val, lengths):
    pos = 0
    skip = 0
    size_of = len(val)
    for _ in xrange(64):
        for l in lengths:
            mid = l//2
            for idx in xrange(mid):
                val[(pos+l-idx-1) % size_of], val[(pos+idx) % size_of] = val[(pos+idx) % size_of], val[(pos+l-idx-1) % size_of]

            pos = (pos + l + skip) % size_of
            skip += 1

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

    return hsh

print solve_challenge2(range(256), map(ord, "")+[17, 31, 73, 47, 23])
print solve_challenge2(range(256), map(ord, "AoC 2017")+[17, 31, 73, 47, 23])
print solve_challenge2(range(256), map(ord, "1,2,3")+[17, 31, 73, 47, 23])
print solve_challenge2(range(256), map(ord, "1,2,4")+[17, 31, 73, 47, 23])
print solve_challenge2(range(256), map(ord, INPUT)+[17, 31, 73, 47, 23])
