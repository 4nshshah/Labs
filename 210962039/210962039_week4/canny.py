import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("./resources/rm.jpg")
img_blur = cv.GaussianBlur(img, (3,3), 0)
edges = cv.Canny(image=img_blur, threshold1=100, threshold2=200)  # Canny Edge Detection

plt.imshow(edges, cmap = 'gist_gray')
plt.title("Canny edge detection")
plt.axis('off')
plt.show()