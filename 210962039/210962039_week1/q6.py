import cv2

img = cv2.imread('car.JPG')
height, width = img.shape[:2]
center = (width/2, height/2)
rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)
rotated_img = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()