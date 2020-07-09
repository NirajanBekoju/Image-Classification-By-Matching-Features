import cv2
import numpy as np
import os

#Vairable Declaration
path = "class"
classes = os.listdir(path)
good_feature_length = []
# print(classes) 

# Creating the oriented ...
orb = cv2.ORB_create(nfeatures=1000)

# Training Image
img2 = cv2.imread('objects/calc.jpeg', 0)

# Function to find the array feature length
def features_length(class_des, training_des):
    global good_feature_length
    # BruteForce Matching of the images
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(class_des, training_des, k = 2)

    good = [] # good features 
    for m,n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    
    good_feature_length.append(len(good))

# Find the id of the class that matches the most with the training object
def find_id_class():
    global good_feature_length
    maximum = max(good_feature_length)
    index = good_feature_length.index(maximum)
    return index 

for class_image in classes:
    # Reading all the class image
    img1 = cv2.imread(f'{path}/{class_image}', 0)

    # Checkin the features keypoints and the description
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    features_length(des1, des2)

# Finding the index of the required object
index_class = find_id_class()

print(classes)
print(good_feature_length)
print(index_class)

cv2.putText(img2, classes[index_class], (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow("Training", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


    

