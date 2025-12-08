# --- Day 8: Playground ---

def part1(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    boxes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    
    n = len(boxes)
    
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = boxes[i]
            x2, y2, z2 = boxes[j]
            dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
            distances.append((dist, i, j))
    
    distances.sort()
    
    parent = list(range(n))
    size = [1] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
        return True
    limit = 1000
    
    pairs_to_process = distances[:limit]
    
    for dist, i, j in pairs_to_process:
        union(i, j)
    
    circuit_sizes = {}
    for i in range(n):
        root = find(i)
        if root not in circuit_sizes:
            circuit_sizes[root] = 0
        circuit_sizes[root] += 1
    
    sizes = sorted(circuit_sizes.values(), reverse=True)
    
    result = 1
    for s in sizes[:3]:
        result *= s
        
    return result


def part2(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    boxes = []
    for line in lines:
        x, y, z = map(int, line.split(','))
        boxes.append((x, y, z))
    
    n = len(boxes)
    
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = boxes[i]
            x2, y2, z2 = boxes[j]
            dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2) ** 0.5
            distances.append((dist, i, j))
    
    distances.sort()
    
    parent = list(range(n))
    size = [1] * n
    components = n  

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        nonlocal components
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return False  
        if size[root_x] < size[root_y]:
            root_x, root_y = root_y, root_x
            
        parent[root_y] = root_x
        size[root_x] += size[root_y]
        components -= 1
        
        return True

    last_critical_connection = None
    
    for dist, i, j in distances:
        if union(i, j):
            last_critical_connection = (i, j)
            
            if components == 1:
                break
    
    if last_critical_connection is None:
        return 0 

    i, j = last_critical_connection
    
    x_i = boxes[i][0]
    x_j = boxes[j][0]
    
    return x_i * x_j
