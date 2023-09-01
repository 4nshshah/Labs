import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
image = cv.imread("./resources/img.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
rho = 1
theta = np.pi / 180
threshold = 250
min_line_length = 50
max_line_gap = 5
gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

low_threshold = 50
high_threshold = 100
edges = cv.Canny(gray, low_threshold, high_threshold)
plt.imshow(edges, cmap='gray')
line_image = np.copy(image)
lines = cv.HoughLinesP(edges, rho, theta, threshold, np.array([]),
                        min_line_length, max_line_gap)

for line in lines:
    for x1, y1, x2, y2 in line:
        cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)

plt.imshow(line_image)
plt.show()