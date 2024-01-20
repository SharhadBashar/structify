from helper import *

class Chords:
    def __init__(self):
        pass

    def chord_mathematical(self, radians, id, radius = 1):
        if (len(radians) % 2 != 0 or len(id) % 2 != 0):
            return False
        
        intersections = 0
        lines = lines_xy(radians, id)
        for line in lines:
            m, b = line_equation(lines[line]['s'], lines[line]['e'])
            lines[line]['equation'] = {'m': m, 'b': b}
        
        line_ids = list(lines.keys())
        for i in range(len(line_ids) - 1):
            for j in range(i + 1, len(line_ids)):
                x, y = line_intersection(
                    (lines[line_ids[i]]['s'], lines[line_ids[i]]['e']),
                    (lines[line_ids[j]]['s'], lines[line_ids[j]]['e'])
                )
                if (intersection_in_circle(x, y)):
                    intersections += 1

        return intersections

    def chord_intersection(self, radians, id):
        if (len(radians) % 2 != 0 or len(id) % 2 != 0):
            return False
        
        intersections = 0
        lines = chord_lines(radians, id)
        line_ids = list(lines.keys())
        for i in range(len(line_ids) - 1):
            for j in range(i + 1, len(line_ids)):
                intersections += intersect(lines[line_ids[i]], lines[line_ids[j]])
        return intersections