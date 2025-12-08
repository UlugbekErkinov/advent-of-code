# --- Day 7: Laboratories ---

def part1(filename):
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f]
    
    start_col = None
    for col in range(len(grid[0])):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        return 0
    
    beams = [(0, start_col)]
    split_count = 0
    
    visited = set()
    
    while beams:
        new_beams = []
        
        for row, col in beams:
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            if row >= len(grid):
                continue
            
            if grid[row][col] == '^':
                split_count += 1
                
                if col - 1 >= 0:
                    new_beams.append((row + 1, col - 1))
                if col + 1 < len(grid[row]):
                    new_beams.append((row + 1, col + 1))
            else:
                if row + 1 < len(grid):
                    new_beams.append((row + 1, col))
        
        beams = new_beams
    
    return split_count


def part2(filename):
    with open(filename, 'r') as f:
        grid = [line.rstrip('\n') for line in f]
    
    start_col = None
    for col in range(len(grid[0])):
        if grid[0][col] == 'S':
            start_col = col
            break
    
    if start_col is None:
        return 0
    
    from collections import defaultdict
    
    current_row_counts = defaultdict(int)
    current_row_counts[start_col] = 1
    
    for row in range(len(grid)):
        next_row_counts = defaultdict(int)
        
        for col, count in current_row_counts.items():
            if col < 0 or col >= len(grid[row]):
                continue
            
            if grid[row][col] == '^':
                if col - 1 >= 0:
                    next_row_counts[col - 1] += count
                if col + 1 < len(grid[row]):
                    next_row_counts[col + 1] += count
            else:
                next_row_counts[col] += count
        
        current_row_counts = next_row_counts
    
    return sum(current_row_counts.values())
