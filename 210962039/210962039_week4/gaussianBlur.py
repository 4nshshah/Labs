import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
image = cv.imread("./resources/rm.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)


kernelSizes = [(7,7),(11,11),(15,15),(23,23)]
fig, axes = plt.subplots(1,len(kernelSizes))
for count, i in enumerate(kernelSizes):
    img = cv.GaussianBlur(image, i,0)
    axes[count].imshow(img)
    axes[count].set_title(f"{i[0]}x{i[1]}")

plt.show()
