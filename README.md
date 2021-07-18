# Image Classification By Matchin Features
This program classify the given image from the web camera into the objects that are trained. 
## Demo
If none of them matched, then no match is shown with red text on the image. If any of the image matched, then they are shown with green text in the image as shown below.
![Screenshot from 2021-07-17 23-32-10](https://user-images.githubusercontent.com/56423554/126074928-32ce8cc3-a877-4b7d-9493-611e1c65a8e9.png)
![Screenshot from 2021-07-17 23-34-28](https://user-images.githubusercontent.com/56423554/126074934-55302c70-f560-484e-9651-62c8795ceb3b.png)

## To Run Locally
**Pull Repository**
```
git pull https://github.com/NirajanBekoju/Image-Classification-By-Matching-Features
```
**Trainee Image**
- Keep the image of the object you want to train in the Class Folder.

**Create Virtual environement and activate it**
```
virtualenv venv
source ./venv/bin/activate
```

**Install requirements**
```
pip install -r requirements.txt 
```

You can run the program by using the webcam or Camera Phone with IP WebCam<br />
**Install IPWebcam App in your android phone** 
- Start Server and Connect Hotspot of mobile with laptop
- Get the url of shot.jpg
- Paste the url in place of url variable in image_classifier_cam.py
