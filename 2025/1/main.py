def part1(filename):
    with open(filename, 'r') as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]  
        distance = int(rotation[1:])  
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    
    return zero_count


def part2(filename):
    with open(filename, 'r') as f:
        rotations = [line.strip() for line in f if line.strip()]
    
    position = 50
    zero_count = 0
    
    for rotation in rotations:
        direction = rotation[0]  
        distance = int(rotation[1:])  
        
        start_pos = position
     
        zeros_this_rotation = distance // 100
        partial_distance = distance % 100
        
        if partial_distance > 0:
            if direction == 'R':
                if start_pos + partial_distance >= 100:
                    zeros_this_rotation += 1    
            elif direction == 'L':
                if start_pos != 0 and start_pos <= partial_distance:
                    zeros_this_rotation += 1
        
        zero_count += zeros_this_rotation
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
            
    return zero_count


try:
    input_file = 'input.txt'
    print("PART 1: {}".format(part1(input_file)))
    print("PART 2: {}".format(part2(input_file)))
except FileNotFoundError:
    print("Error: input.txt not found.")