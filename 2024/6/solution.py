"""
--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?
"""
with open("input.txt", "r") as f:
    puzzle_input = f.readlines()


def part1():
    grid = [list(row) for row in puzzle_input]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    nrows, ncols = len(grid), len(grid[0])

    guard_pos = None
    guard_dir = None
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'
                break
        if guard_pos:
            break

    visited = set()
    visited.add(guard_pos)

    while True:
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        if not (0 <= next_pos[0] < nrows and 0 <= next_pos[1] < ncols):
            break

        if grid[next_pos[0]][next_pos[1]] == '#':
            guard_dir = turn_right[guard_dir]
        else:
            guard_pos = next_pos
            visited.add(guard_pos)

    return len(visited)


def part2():
    grid = [list(row) for row in puzzle_input]
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    nrows, ncols = len(grid), len(grid[0])
    guard_pos = None
    guard_dir = None
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                grid[r][c] = '.'
                break
        if guard_pos:
            break

    def simulate(grid, start_pos, start_dir):
        visited_states = set()
        guard_pos = start_pos
        guard_dir = start_dir
        while True:

            state = (guard_pos, guard_dir)
            if state in visited_states:
                return True

            visited_states.add(state)

            dr, dc = directions[guard_dir]
            next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

            if not (0 <= next_pos[0] < nrows and 0 <= next_pos[1] < ncols):
                return False

            if grid[next_pos[0]][next_pos[1]] == '#':
                guard_dir = turn_right[guard_dir]
            else:
                guard_pos = next_pos

    loop_positions = 0
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == '.' and (r, c) != guard_pos:
                grid[r][c] = '#'
                if simulate(grid, guard_pos, guard_dir):
                    loop_positions += 1
                grid[r][c] = '.'

    return loop_positions


print("Part 1:", part1())
print("Part 2:", part2())