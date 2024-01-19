from draw import draw
from chords import chord_intersection
from mathematical import chord_mathematical

if __name__ == '__main__':
    radians = [0.5, 0.78, 1.47, 1.77, 2.56, 3.00, 3.92, 5.00]
    id =      ['s1', 's2', 's3', 'e2', 's4', 'e1', 'e3', 'e4']
    # radians = [0.78, 1.47, 1.77, 3.92]
    # id =      ['s1', 's2', 'e1', 'e2']
    draw(radians, id)
    
    print('Mathematical Intersections:', chord_mathematical(radians, id))
    print('Intersections:', chord_intersection(radians, id))