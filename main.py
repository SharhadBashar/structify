from draw import draw
from chords import Chords

if __name__ == '__main__':
    radians = [0.5, 0.78, 1.47, 1.77, 2.56, 3.00, 3.92, 5.00]
    id =      ['s1', 's2', 's3', 'e2', 's4', 'e1', 'e3', 'e4']
    # radians = [0.78, 1.47, 1.77, 3.92]
    # id =      ['s1', 's2', 'e1', 'e2']
    draw(radians, id)
    
    print('Intersections using mathematical method:', Chords().chord_mathematical(radians, id))
    print()
    print('Intersections:', Chords().chord_intersection(radians, id))
