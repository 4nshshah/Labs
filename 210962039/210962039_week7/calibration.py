import numpy as np
import cv2
import glob

# Define the chessboard dimensions (number of internal corners)
chessboard_size = (9, 6)

# Prepare object points (coordinates of chessboard corners in 3D space)
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# Lists to store object points and image points from all images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Load and process calibration images
images = glob.glob('./resources/*.jpg')  # Change this to your image directory

for image_file in images:
    print("started")
    img = cv2.imread(image_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)

    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)
    print("finished")
# Calibrate the camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Save calibration results for future use
np.savez("calibration_data.npz", mtx=mtx, dist=dist)

# Undistort an example image
example_image = cv2.imread('./resources/example.jpg')  # Load an example image
undistorted_image = cv2.undistort(example_image, mtx, dist, None, mtx)

# Display the original and undistorted images
cv2.imshow("Original Image", example_image)
cv2.imshow("Undistorted Image", undistorted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
