# --- Day 2: Gift Shop ---s

def part1(filename):
    def is_invalid(num):
        s = str(num)
        length = len(s)
        
        if length % 2 != 0:
            return False
        
        mid = length // 2
        return s[:mid] == s[mid:]
    
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    ranges_str = content.replace('\n', '').replace(' ', '')
    range_parts = ranges_str.split(',')
    
    total_sum = 0
    
    for range_str in range_parts:
        if not range_str:
            continue
        
        start, end = map(int, range_str.split('-'))
        
        for num in range(start, end + 1):
            if is_invalid(num):
                total_sum += num
    
    return total_sum


def part2(filename):
    def is_invalid(num):
        s = str(num)
        length = len(s)
        
        for pattern_len in range(1, length // 2 + 1):
            if length % pattern_len != 0:
                continue
            
            pattern = s[:pattern_len]
            if pattern * (length // pattern_len) == s:
                return True
        
        return False
    
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    ranges_str = content.replace('\n', '').replace(' ', '')
    range_parts = ranges_str.split(',')
    
    total_sum = 0
    
    for range_str in range_parts:
        if not range_str:
            continue
        
        start, end = map(int, range_str.split('-'))
        
        for num in range(start, end + 1):
            if is_invalid(num):
                total_sum += num
    
    return total_sum
