# Real Time Road Lane Detection System
## Project overview
* Autonomous Driving Car is one of the most disruptive innovations in AI. An autonomous car can go anywhere a traditional car can go and does everything that an experienced human driver does. But it’s very essential to train it properly. One of the many steps involved during the training of an autonomous driving car is lane detection, which is the preliminary step.

* The primary goal of this project is to develop a Road Lane Detection System that accurately identifies and tracks road lanes in real-time using computer vision and machine learning techniques. This system is intended to enhance the safety and efficiency of autonomous vehicles and advanced driver-assistance systems (ADAS).

## Steps Involved
* Input image
* Create the camera caliberation matrix and distortion coefficient and undistort the image
* Applying perspective transform
* Thresholding to extract the lane lines
* Histogram peak detection
* Applying sliding window search algorithm ot detect lane lines
* Apply curve fitting
* Overlay the detected lane lines and output the image

