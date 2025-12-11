import re
from functools import lru_cache

def part1(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    graph = {}
    for line in content.strip().split('\n'):
        if not line:
            continue
        match = re.match(r'(\w+): (.*)', line)
        if match:
            source = match.group(1)
            targets = match.group(2).split()
            graph[source] = targets

    memo = {}

    def count_paths(node):
        if node == 'out':
            return 1
            
        if node in memo:
            return memo[node]

        if node not in graph:
            return 0

        current_paths = 0
        for neighbor in graph[node]:
            current_paths += count_paths(neighbor)
        
        memo[node] = current_paths
        return current_paths

    total_paths = count_paths('you')
    return total_paths


def part2(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    graph = {}
    for line in content.strip().split('\n'):
        if not line:
            continue
        match = re.match(r'(\w+): (.*)', line)
        if match:
            source = match.group(1)
            targets = match.group(2).split()
            graph[source] = tuple(targets)
    
    @lru_cache(maxsize=None)
    def count_paths(node, visited_dac, visited_fft):
        if node == 'dac':
            visited_dac = True
        if node == 'fft':
            visited_fft = True
        
        if node == 'out':
            return 1 if (visited_dac and visited_fft) else 0
        
        if node not in graph:
            return 0
        
        total = 0
        for neighbor in graph[node]:
            total += count_paths(neighbor, visited_dac, visited_fft)
        
        return total
    
    result = count_paths('svr', False, False)
    return result
