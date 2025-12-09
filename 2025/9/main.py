# --- Day 9: Movie Theater ---

def part1(filename):
    with open(filename, 'r') as f:
        coords = f.read().split()
    
    max_area = 0
    
    for i in range(len(coords)):
        start = list(map(int, coords[i].split(',')))
        for j in range(i + 1, len(coords)):
            end = list(map(int, coords[j].split(',')))
            area = abs(start[0] - end[0] + 1) * abs(start[1] - end[1] + 1)
            if area > max_area:
                max_area = area
    
    return max_area


def part2(filename):
    def check_vertex_overlap(rect_bounds, points):
        rx1, rx2, ry1, ry2 = rect_bounds
        for px, py in points:
            if rx1 < px < rx2 and ry1 < py < ry2:
                return True
        return False
    
    def check_edge_crossing(rect_bounds, edges):
        rx1, rx2, ry1, ry2 = rect_bounds
        for ex1, ey1, ex2, ey2 in edges:
            if ex1 == ex2:
                if rx1 < ex1 < rx2:
                    edge_y_min, edge_y_max = min(ey1, ey2), max(ey1, ey2)
                    if edge_y_min <= ry1 and edge_y_max >= ry2:
                        return True
            else:
                if ry1 < ey1 < ry2:
                    edge_x_min, edge_x_max = min(ex1, ex2), max(ex1, ex2)
                    if edge_x_min <= rx1 and edge_x_max >= rx2:
                        return True
        return False
    
    with open(filename, 'r') as f:
        data = f.read()
    
    points = []
    for line in data.strip().splitlines():
        parts = line.split(',')
        points.append((int(parts[0]), int(parts[1])))
    
    n = len(points)
    
    edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1[0], p1[1], p2[0], p2[1]))
    
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            rx1, rx2 = min(x1, x2), max(x1, x2)
            ry1, ry2 = min(y1, y2), max(y1, y2)
            
            width = rx2 - rx1 + 1
            height = ry2 - ry1 + 1
            area = width * height
            
            if area <= max_area:
                continue
            
            rect_bounds = (rx1, rx2, ry1, ry2)
            
            if check_vertex_overlap(rect_bounds, points):
                continue
            
            if check_edge_crossing(rect_bounds, edges):
                continue
            
            max_area = area
    
    return max_area
