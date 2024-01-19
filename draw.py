import numpy as np
import matplotlib.pyplot as plt

from helper import *

def draw(radians, id, radius = 1):
    theta = np.linspace(0, 2 * np.pi)
    a = radius * np.cos(theta)
    b = radius * np.sin(theta)
    
    lines = lines_xy(radians, id)

    figure, axes = plt.subplots()
    axes.set_aspect(1)
    
    for line in lines:
        line = lines[line]
        plt.plot([line['s'][0], line['e'][0]], [line['s'][1], line['e'][1]], 'ro-')
    plt.plot(a, b)
    
    plt.title('Chords')
    plt.show()
