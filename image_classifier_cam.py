import cv2
import requests
import numpy as np
import os

#Vairable Declaration
url = "http://192.168.43.1:8080/shot.jpg"
frame_width = 900
frame_height = 560

path = "class"
classes = os.listdir(path) # List of all trainee images
threshold_matching = 20
# Creating the oriented ...
orb = cv2.ORB_create(nfeatures=1000)

# Defining window
cv2.namedWindow("Android Cam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Android Cam", frame_width, frame_height)

# Collecting the name of the ttrainee image
class_name = []
for name in classes:
    class_name.append(name.split('.')[0])

# Function to find the array feature length
def features_length(img1, img2):
    global good_feature_length
    # Checkin the features keypoints and the description
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # BruteForce Matching of the images
    bf = cv2.BFMatcher()
    good = [] # good features 
    try:    
        matches = bf.knnMatch(des1, des2, k = 2)    
        for m,n in matches:
            if m.distance < 0.75 * n.distance:
                good.append([m])
    except:
        pass
    good_feature_length.append(len(good))

# Find the id of the class that matches the most with the training object
def find_id_class():
    global good_feature_length
    maximum = max(good_feature_length)
    index = good_feature_length.index(maximum)
    return index 

# Retrieving the video from webcam
while True:
    timer1 = cv2.getTickCount()
    good_feature_length = []
    # Retrieving the image from the url
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img2 = cv2.imdecode(img_arr, -1)
    
    gray_original = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    for class_image in classes:
        # Reading all the class image
        img1 = cv2.imread(f'{path}/{class_image}', 0)
        features_length(img1, gray_original)

    # Finding the index of the required object
    print(good_feature_length)
    index_class = find_id_class()
    print(index_class)
    if good_feature_length[index_class] > threshold_matching:
        cv2.putText(img2, class_name[index_class], (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(img2,"No Match" , (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow("Android Cam", img2)
    
    timer2 = cv2.getTickCount()
    time = (timer2 - timer1)/ cv2.getTickFrequency()
    print(f'time: {time}s')
    # Condition for the breakage
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
