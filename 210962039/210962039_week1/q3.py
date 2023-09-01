import cv2 as cv
import numpy as np
img = np.zeros((512, 512, 3), np.uint8)
img1 = cv.imread('C:/Users/OSLAB/Desktop/210962170/car.JPG')
my_rect = cv.rectangle(img1, (0, 0), (511, 511), (255, 0, 0), 5)
cv.imshow('Rectangle', my_rect)
cv.waitKey(0)
cv.destroyAllWindows()

