def chord_lines(radians, id):
    lines = {}
    for i in range(len(id)):
        line_id = id[i][1]
        rad = radians[i]
        if (line_id not in lines.keys()):
            lines[line_id] = [-1, -1]    
        if (id[i][0] == 's'):
            lines[line_id][0] = radians[i]
        else:
            lines[line_id][1] = radians[i]
    return lines

def intersect(line_1, line_2):
    if (line_1[0] <= line_2[0] and line_1[1] >= line_2[0] and line_1[1] <= line_2[1]):
        return 1
    return 0

def chord_intersection(radians, id):
    if (len(radians) % 2 != 0 or len(id) % 2 != 0):
        return False
    
    intersections = 0
    lines = chord_lines(radians, id)
    line_ids = list(lines.keys())
    for i in range(len(line_ids) - 1):
        for j in range(i + 1, len(line_ids)):
            intersections += intersect(lines[line_ids[i]], lines[line_ids[j]])
    return intersections