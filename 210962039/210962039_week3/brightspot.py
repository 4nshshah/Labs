import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("resources/reference.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
(minval, maxval, minloc, maxloc) = cv.minMaxLoc(img)

cv.circle(img, maxloc, 5,(0,254,0),2)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()