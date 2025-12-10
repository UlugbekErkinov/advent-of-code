import re

def part1(filename):
    def _machine(target, buttons):
        n_lights = len(target)
        n_buttons = len(buttons)
        
        min_presses = float('inf')
        
        for mask in range(1 << n_buttons):
            state = [0] * n_lights
            presses = 0
            
            for i in range(n_buttons):
                if mask & (1 << i):
                    presses += 1
                    for light in buttons[i]:
                        state[light] ^= 1
            
            if state == target:
                min_presses = min(min_presses, presses)
        
        return min_presses if min_presses != float('inf') else 0
    
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    
    for line in lines:
        lights_match = re.search(r'\[([.#]+)\]', line)
        if not lights_match:
            continue
        
        lights_str = lights_match.group(1)
        target = [1 if c == '#' else 0 for c in lights_str]
        
        button_matches = re.findall(r'\(([0-9,]+)\)', line)
        buttons = []
        for button_str in button_matches:
            button_lights = [int(x) for x in button_str.split(',')]
            buttons.append(button_lights)
        
        min_presses = _machine(target, buttons)
        total_presses += min_presses
    
    return total_presses


def part2(filename):
    from scipy.optimize import linprog
    def _joltage(targets, buttons):
        n_counters = len(targets)
        n_buttons = len(buttons)
        
        A_eq = []
        for counter_idx in range(n_counters):
            row = []
            for button in buttons:
                row.append(1 if counter_idx in button else 0)
            A_eq.append(row)
        
        c = [1] * n_buttons
        
        b_eq = targets
        
        result = linprog(c=c, A_eq=A_eq, b_eq=b_eq, integrality=1, method='highs')
        
        if result.success:
            return int(result.fun)
        
        return 0
    
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    total_presses = 0
    
    for line in lines:
        joltage_match = re.search(r'\{([0-9,]+)\}', line)
        if not joltage_match:
            continue
        
        joltage_str = joltage_match.group(1)
        targets = [int(x) for x in joltage_str.split(',')]
        
        button_matches = re.findall(r'\(([0-9,]+)\)', line)
        buttons = []
        for button_str in button_matches:
            button_counters = [int(x) for x in button_str.split(',')]
            buttons.append(button_counters)
        
        min_presses = _joltage(targets, buttons)
        total_presses += min_presses
    
    return total_presses
