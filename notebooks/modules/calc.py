import math
import numpy as np
import cv2

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


#point (x,y) center (x,y) angle in degrees
def rotate_point(point, center, angle):
  s = math.sin(math.radians(angle))
  c = math.cos(math.radians(angle))
  point = np.array(point)

  #translate point back to origin:
  point[0] = point[0] - center[0]
  point[1] = point[1] - center[1]

  #rotate point
  xnew = point[0] * c - point[1] * s
  ynew = point[0] * s + point[1] * c

  #translate point back:
  point2 = [0,0]
  point2[0] = xnew + center[0]
  point2[1] = ynew + center[1]
  return point2

def rotate_image(image, center, angle):
    rot_mat = cv2.getRotationMatrix2D(center,-angle,1.0)
    new_image = cv2.warpAffine(image, rot_mat, (image.shape[0],image.shape[1]))
    return new_image
