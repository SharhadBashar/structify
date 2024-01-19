import math

'''
line = {
    's': ,
    'e': ,
    'equation': {'m':, 'b':}
}
'''

def lines_xy(radians, id):
    lines = {}    
    for i in range(len(id)):
        line_id = id[i][1]
        rad = radians[i]
        if (line_id not in lines.keys()):
            lines[line_id] = {}    
        if (id[i][0] == 's'):
            lines[line_id]['s'] = (math.cos(rad), math.sin(rad))
        else:
            lines[line_id]['e'] = (math.cos(rad), math.sin(rad))
    return lines

def line_equation(s, e):
    m = (e[1] - s[1]) / (e[0] - s[0])
    b = s[1] - m * s[0]
    return m, b

def line_intersection(l_1, l_2):
    def delta(a, b):
        return a[0] * b[1] - a[1] * b[0]
    
    x_diff = (l_1[0][0] - l_1[1][0], l_2[0][0] - l_2[1][0])
    y_diff = (l_1[0][1] - l_1[1][1], l_2[0][1] - l_2[1][1])

    div = delta(x_diff, y_diff)
    if (div == 0):
       return None, None

    d = (delta(*l_1), delta(*l_2))
    x = delta(d, x_diff) / div
    y = delta(d, y_diff) / div
    return x, y

def intersection_in_circle(x, y, radius = 1):
    if not x or not y:
        return False
    return (x ** 2 + y ** 2) <= radius
