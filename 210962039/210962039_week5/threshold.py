import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread("./resources/img.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

ret, bin = cv.threshold(gray, 120,255, cv.THRESH_BINARY)
ret, binInv = cv.threshold(gray, 120,255, cv.THRESH_BINARY_INV)
ret, trunc = cv.threshold(gray, 120,255, cv.THRESH_TRUNC)
ret, zero = cv.threshold(gray, 120,255, cv.THRESH_TOZERO)
ret, zeroInv = cv.threshold(gray, 120,255, cv.THRESH_TOZERO_INV)
t = [bin, binInv, trunc, zero, zeroInv]
fig, ax = plt.subplots(5,1)
for count,i in enumerate(t):
    ax[count].imshow(i, cmap = 'gist_gray')
plt.show()
