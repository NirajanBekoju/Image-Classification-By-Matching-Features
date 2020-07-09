import cv2
import numpy as np

# Creating the oriented ...
orb = cv2.ORB_create(nfeatures=1000)

# Importing the images
img1 = cv2.imread('class/quee.jpg', 0)
img2 = cv2.imread('objects/queen.jpeg', 0)

# Detection and computation of the common features
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k = 2)

good = []
for m,n in matches:
    if m.distance < 0.75 * n.distance:
        good.append([m])
print(len(good))

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)
# Showing the images
# cv2.imshow("Class", img1)
# cv2.imshow("Objects", img2)
cv2.imshow("image3", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
