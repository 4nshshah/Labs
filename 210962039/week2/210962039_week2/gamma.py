import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('doggy.png')
gamma = [0.2,0.6,1.2,1.6]

figure, axes = plt.subplots(4,figsize = (2,8))

for g in range(len(gamma)):
    new = np.array(255*(img/255)**gamma[g], dtype = 'uint8')
    #cv.imwrite(f"gammaCorrected_{gamma[g]}.png", new)
    axes[g].imshow(new)
    axes[g].axis('off')
    axes[g].set_title(f"Gamma = {gamma[g]}", fontsize = 8)
plt.show()
