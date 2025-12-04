# --- Day 4: Printing Department ---

def part1(filename):
    def count_adjacent_rolls(grid, row, col):
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                r, c = row + dr, col + dc
                
                if 0 <= r < rows and 0 <= c < cols:
                    if grid[r][c] == '@':
                        count += 1
        
        return count
    
    with open(filename, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]
    
    accessible_count = 0
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                adjacent = count_adjacent_rolls(grid, row, col)
                if adjacent < 4:
                    accessible_count += 1
    
    return accessible_count


def part2(filename):
    def count_adjacent_rolls(grid, row, col):
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                r, c = row + dr, col + dc
                
                if 0 <= r < rows and 0 <= c < cols:
                    if grid[r][c] == '@':
                        count += 1
        
        return count
    
    with open(filename, 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    
    total_removed = 0
    
    while True:
        accessible = []
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '@':
                    adjacent = count_adjacent_rolls(grid, row, col)
                    if adjacent < 4:
                        accessible.append((row, col))
        
        if not accessible:
            break
        
        for row, col in accessible:
            grid[row][col] = '.'
        
        total_removed += len(accessible)
    
    return total_removed
