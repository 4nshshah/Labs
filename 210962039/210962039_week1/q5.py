import cv2
import numpy as np

img = cv2.imread('car.JPG')
print(img.shape)
half = cv2.resize(img, (0, 0), fx=0.1, fy=0.1)
print(half.shape)
bigger = cv2.resize(img, (1050,1050), fx=3, fy=3)
cv2.imshow('downsize', half)
cv2.waitKey(0)
cv2.imshow('upsize', bigger)
cv2.waitKey(0)



