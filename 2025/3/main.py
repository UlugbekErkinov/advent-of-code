# --- Day 3: Secret Bank ---

def part1(filename):
    def max_joltage(bank):
        max_value = 0
        
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                value = int(bank[i] + bank[j])
                max_value = max(max_value, value)
        
        return max_value
    
    with open(filename, 'r') as f:
        banks = [line.strip() for line in f if line.strip()]
    
    total_joltage = 0
    
    for bank in banks:
        joltage = max_joltage(bank)
        total_joltage += joltage
    
    return total_joltage


def part2(filename):
    def max_joltage(bank):
        n = len(bank)
        to_skip = n - 12
        
        result = []
        skip_count = 0
        i = 0
        
        while len(result) < 12:

            can_skip = to_skip - skip_count
            
            best_digit = '0'
            best_pos = i
            
            max_look_ahead = min(i + can_skip + 1, n)
            
            for j in range(i, max_look_ahead):
                if bank[j] > best_digit:
                    best_digit = bank[j]
                    best_pos = j
            
            result.append(best_digit)
            skip_count += (best_pos - i)
            i = best_pos + 1
        
        return int(''.join(result))
    
    with open(filename, 'r') as f:
        banks = [line.strip() for line in f if line.strip()]
    
    total_joltage = 0
    
    for bank in banks:
        joltage = max_joltage(bank)
        total_joltage += joltage
    
    return total_joltage
