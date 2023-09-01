import cv2 as cv
import numpy as np

img = cv.imread('doggy.png')
c = 255/(np.log(1+np.max(img)))
log = c*np.log(1+img)
log = np.array(log, dtype = np.uint8)
cv.imwrite("log_transformed_doggy.png", log)
cv.imshow('log', log)
cv.waitKey(0)
cv.destroyAllWindows()