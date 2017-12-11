with open("input.txt", "r") as f:
    INPUT = f.read()

def solve_challenge1(val):
    distance = 1
    nr_elements = 1
    furthest_points = (1,1,1,1)

    while nr_elements < val:
        distance += 2
        furthest_points = (nr_elements+1*(distance-1), nr_elements+2*(distance-1), nr_elements+3*(distance-1), nr_elements+4*(distance-1))
        nr_elements += 4*(distance-1)

    closest_points = map(lambda x: x - distance//2, furthest_points)
    return min(map(lambda x: abs(val-x), closest_points)) + distance//2


print solve_challenge1(INPUT)


def spiral(N, M):
    x, y = 0,0
    dx, dy = 0, -1

    for dumb in xrange(N*M):
        if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1-x:
            dx, dy = -dy, dx

        if abs(x) > N/2 or abs(y) > M/2:
            dx, dy = -dy, dx
            x, y = -y+dx, x+dy

        yield x, y
        x, y = x+dx, y+dy


def get_neighbors(maxx, maxy):
    return lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                              for y2 in range(y - 1, y + 2)
                              if (-1 < x <= maxx and
                                  -1 < y <= maxy and
                                  (x != x2 or y != y2) and
                                  (0 <= x2 <= maxx) and
                                  (0 <= y2 <= maxy))]


def solve_challenge2(val):
    grid_size = 9
    grid = [[0]*grid_size for _ in xrange(grid_size)]

    for x,y in spiral(grid_size, grid_size):
        transformed_x = x+grid_size//2
        transformed_y = y+grid_size//2

        new_value = max(1, sum(map(lambda coord: grid[coord[0]][coord[1]], get_neighbors(grid_size-1, grid_size-1)(transformed_x, transformed_y))))
        grid[transformed_x][transformed_y] = new_value

        if new_value > val:
            return new_value


print solve_challenge2(INPUT)
