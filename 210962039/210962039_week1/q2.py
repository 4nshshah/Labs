import cv2
import numpy as np

my_img = cv2.imread('car.JPG')
cv2.imshow('Reference Image', my_img)
px = my_img[250,250]
print(px)
cv2.waitKey(0)
cv2.destroyAllWindows()
