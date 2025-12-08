# --- Day 6: Trash Compactor ---

from functools import reduce

def parse_problems(lines):
    if not lines:
        return []

    max_width = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_width) for line in lines]
    
    data_rows = padded_lines[:-1]
    operator_row = padded_lines[-1]
    num_rows = len(data_rows)
    
    problems = []
    current_problem_cols = []
    in_problem = False
    
    for col_index in range(max_width):
        col_chars = [data_rows[r][col_index] for r in range(num_rows)]
        is_space_col = all(c == ' ' for c in col_chars)
        
        if not is_space_col:
            current_problem_cols.append(col_index)
            in_problem = True
        elif is_space_col and in_problem:
            op = ''
            for c_idx in current_problem_cols:
                if operator_row[c_idx] != ' ':
                    op = operator_row[c_idx]
                    break
            
            problems.append({
                'columns': current_problem_cols,
                'operator': op
            })
            current_problem_cols = []
            in_problem = False
            
    if current_problem_cols:
        op = ''
        for c_idx in current_problem_cols:
            if operator_row[c_idx] != ' ':
                op = operator_row[c_idx]
                break
        problems.append({
            'columns': current_problem_cols,
            'operator': op
        })

    return problems, padded_lines

def _oper(numbers, op):
    if not numbers:
        return 0
    
    if op == '+':
        return sum(numbers)
    elif op == '*':
        return reduce(lambda a, b: a * b, numbers)
    return 0


def part1(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]
    
    problems, padded_lines = parse_problems(lines)
    data_rows = padded_lines[:-1]
    
    grand_total = 0
    
    for problem in problems:
        problem_cols = problem['columns']
        op = problem['operator']

        numbers = []
        for row in data_rows:
            start_col = problem_cols[0]
            end_col = problem_cols[-1]
            
            num_str = row[start_col : end_col + 1].replace(' ', '')
            if num_str:
                numbers.append(int(num_str))
        
        answer = _oper(numbers, op)
        grand_total += answer
        
    return grand_total

def part2(filename):
    with open(filename, 'r') as f:
        lines = [line.strip('\n') for line in f]
    
    problems, padded_lines = parse_problems(lines)
    data_rows = padded_lines[:-1]
    
    grand_total = 0

    problems.reverse() 
    
    for problem in problems:
        problem_cols = problem['columns']
        op = problem['operator']
        
        problem_numbers = []
        for col_index in problem_cols:
            number_digits = []
            for row in data_rows:
                char = row[col_index]
                if char.isdigit():
                    number_digits.append(char)
            
            num_str = "".join(number_digits)
            if num_str:
                problem_numbers.append(int(num_str))
        
        answer = _oper(problem_numbers, op)
        grand_total += answer
        
    return grand_total
