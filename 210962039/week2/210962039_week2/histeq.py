import cv2
import matplotlib.pyplot as plt
import numpy as np

# read a image using imread
img = cv2.imread('doggy.png', 0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
fig, axes = plt.subplots(2,2, figsize = (12,8))
axes[0,0].plot(cdf_normalized, color = 'b')
axes[0,0].hist(img.flatten(),256,[0,256], color = 'r')
axes[0,0].set_title('Original Image')
axes[0,0].set_xlim([0,256])
axes[0,0].legend(('cdf','histogram'), loc = 'upper left')

axes[0,1].imshow(img, cmap = 'Greys')

equ = cv2.equalizeHist(img)

hist,bins = np.histogram(equ.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
axes[1,0].plot(cdf_normalized, color = 'b')
axes[1,0].hist(equ.flatten(),256,[0,256], color = 'r')
axes[1,0].set_xlim([0,256])
axes[1,0].legend(('cdf','histogram'), loc = 'upper left')
axes[1,0].set_title('Equalised Image')

axes[1,1].imshow(equ, cmap = 'Greys')
plt.show()
