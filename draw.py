import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt

from helper import *

def draw(radians, id, radius = 1):
    intersections = []
    theta = np.linspace(0, 2 * np.pi)
    circle_a = radius * np.cos(theta)
    circle_b = radius * np.sin(theta)
    
    lines = lines_xy(radians, id)
    for line in lines:
        m, b = line_equation(lines[line]['s'], lines[line]['e'])
        lines[line]['equation'] = 'y = {}*x + {}'.format(m, b)
        
    line_ids = list(lines.keys())
    for i in range(len(line_ids) - 1):
        for j in range(i + 1, len(line_ids)):
            x, y = line_intersection(
                (lines[line_ids[i]]['s'], lines[line_ids[i]]['e']),
                (lines[line_ids[j]]['s'], lines[line_ids[j]]['e'])
            )
            if (intersection_in_circle(x, y)):
                intersections.append((x, y))
   
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    
    for line in lines:
        line = lines[line]
        plt.plot([line['s'][0], line['e'][0]], [line['s'][1], line['e'][1]], 'ro-')
    for intersection in intersections:
        plt.plot(intersection[0], intersection[1], 'bo')
        
    print('Lines ({}) Start and End point as well as equation:'.format(len(lines)))
    pprint(lines)
    print()
    print('List of valid intersections:')
    pprint(intersections)
    print()
    
    plt.plot(circle_a, circle_b)
    
    plt.title('Chords')
    plt.show()
