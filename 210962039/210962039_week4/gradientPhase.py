import numpy as np

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./resources/rm.jpg')
cv2.imshow('Original', img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
imgn = np.array(img_gray, float)
fig, ax = plt.subplots(figsize = (12,8),nrows=1,ncols=2)
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)

# grad = sobelx**2 + sobely**2
# grad = np.sqrt(grad)

grad = np.hypot(sobelx, sobely)
grad = (grad - grad.min())/(grad.max() - grad.min()) * 255
final = imgn+grad
phase = cv2.phase(sobelx, sobely, angleInDegrees=True)
phaseAngle = np.arctan(sobelx, sobely)
# cv2.imshow("final", final)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

ax[0].imshow(grad, cmap ='gist_gray')
ax[1].imshow(final, cmap ='gist_gray')
ax[0].set_title("Gradient")
ax[1].set_title("Final Image")
plt.show()
fig2, ax2 = plt.subplots(figsize = (12,8),nrows=1,ncols=2)
ax2[0].imshow(phase, cmap ='gist_gray')
ax2[1].imshow(phaseAngle, cmap ='gist_gray')
ax2[0].set_title("OpenCV Phase angle using phase()")
ax2[1].set_title("Numpy Phase angle using arctan()")
plt.show()
plt.show()