
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Reading the image
image = cv2.imread('../week2/210962039_week2/doggy.png')

# Creating the kernel(2d convolution matrix)

kernelSizes = [(3,3),(5,5),(7,7),(11,11)]
fig, axes = plt.subplots(1,len(kernelSizes))

for count, i in enumerate(kernelSizes):
    kernel1 = np.ones(i, np.float32) / i[0]**2
    img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
    axes[count].imshow(img)
    axes[count].set_title(f"{i[0]}x{i[1]}")
# Shoeing the original and output image

plt.show()
