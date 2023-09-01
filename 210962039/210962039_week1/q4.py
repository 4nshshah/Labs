import cv2 as cv
import numpy as np

img_grayscale = cv.imread('C:/Users/OSLAB/Desktop/210962170/car.JPG')
r = cv.split(img_grayscale) #this returns 3D array of
zeros = np.zeros(r[0].shape, np.uint8)
img_red = cv.merge((zeros, zeros, r[2]))
img_green = cv.merge((zeros, r[1], zeros))
img_blue = cv.merge((r[0], zeros, zeros))


cv.imshow('Green', img_green)
cv.waitKey(0)
cv.imshow('Blue', img_blue)
cv.waitKey(0)
cv.imshow('Red', img_red)
cv.waitKey(0)

cv.destroyAllWindows()

