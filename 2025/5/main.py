# --- Day 5: Cafeteria ---

def part1(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    
    blank_index = lines.index('')
    
    ranges_section = lines[:blank_index]
    ids_section = lines[blank_index + 1:]
    
    ranges = []
    for line in ranges_section:
        if line: 
            start, end = map(int, line.split('-'))
            ranges.append((start, end))

    ingredient_ids = []
    for line in ids_section:
        if line:
            ingredient_ids.append(int(line))
    
    fresh_count = 0
    for ingredient_id in ingredient_ids:
        for start, end in ranges:
            if start <= ingredient_id <= end:
                fresh_count += 1
                break
    
    return fresh_count


def part2(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f]
    
    blank_index = lines.index('')
    ranges_section = lines[:blank_index]
    
    ranges = []
    for line in ranges_section:
        if line:
            start, end = map(int, line.split('-'))
            ranges.append((start, end))
    
    ranges.sort()
    
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    total_count = 0
    for start, end in merged:
        total_count += (end - start + 1)
    
    return total_count
