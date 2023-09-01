import matplotlib.pyplot as plt
from skimage import exposure
import cv2

src = cv2.imread("resources/img_1.png")
ref = cv2.imread("resources/img_2.png")
# src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY)
multi = True if src.shape[-1] > 1 else False
matched = exposure.match_histograms(src, ref, channel_axis=multi)
# show the output images
cv2.imshow("Source", src)
cv2.imshow("Reference", ref)
cv2.imshow("Matched", matched)
cv2.waitKey(0)


(fig, axs) = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))

for (i, image) in enumerate((src, ref, matched)):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	for (j, color) in enumerate(("red", "green", "blue")):
		(hist, bins) = exposure.histogram(image[..., j],source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)
		axs[j, 0].set_ylabel(color)

# set the axes titles
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")
# display the output plots
plt.tight_layout()
plt.show()