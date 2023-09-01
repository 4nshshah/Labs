import numpy as np

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./resources/rm.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
imgn = np.array(img_gray, float)
fig, ax = plt.subplots(figsize = (12,8),nrows=2,ncols=2)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
laplace = cv2.Laplacian(src = img_blur, ddepth=cv2.CV_64F)

xSharp = imgn + (imgn - sobelx)
ySharp = imgn + (imgn - sobely)
xySharp = imgn + (imgn - sobelxy)
laplaceSharp = imgn + (imgn - laplace)

# ax[0][0].imshow(sobelx, cmap ='gist_gray')
# ax[0][1].imshow(sobely, cmap ='gist_gray')
# ax[1][0].imshow(sobelxy, cmap ='gist_gray')
# ax[1][1].imshow(laplace, cmap ='gist_gray')

ax[0][0].imshow(xSharp, cmap ='gist_gray')
ax[0][1].imshow(ySharp, cmap ='gist_gray')
ax[1][0].imshow(xySharp, cmap ='gist_gray')
ax[1][1].imshow(laplaceSharp, cmap ='gist_gray')
ax[0][0].set_title("Sobelx")
ax[0][1].set_title("Sobely")
ax[1][0].set_title("Sobelxy")
ax[1][1].set_title("Laplace")
plt.grid(False)
plt.show()

grad = sobelx**2 + sobely**2
grad = np.sqrt(grad)
grad = (grad - grad.min())/(grad.max() - grad.min()) * 255

cv2.imshow("gradient",imgn  - grad)
cv2.waitKey(0)
cv2.destroyAllWindows()

