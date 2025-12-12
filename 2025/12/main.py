# --- Day 12: Christmas Tree Farm ---

def part1(filename):
    *shapes, regions = open(filename).read().split('\n\n')
    shapes = [s.count('#') for s in shapes]

    res = 0
    for region in regions.strip().split('\n'):
        size, quants = region.split(': ')
        area = eval(size.replace('x', '*'))
        quants = eval(quants.replace(' ', ','))
        total = sum(a*b for a,b in zip(quants, shapes))
        if total < area: 
            res += 1

    return res

def part2(filename):
    pass
