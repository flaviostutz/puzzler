import math

#calculate the angle at point [1] formed by edges with [0] and [2]
def angle_between_points(points):
    a = points[0]
    b = points[1]
    c = points[2]
    
    m1 = (b[1]-a[1])/(b[0]-a[0])
    m2 = (c[1]-b[1])/(c[0]-b[0])

    tgb = (m2-m1)/(1+m1*m2)
    
    return math.degrees(math.atan(tgb))


def is_near(value1, value2, diff):
    err = abs(value1 - value2)
    return err<=diff

