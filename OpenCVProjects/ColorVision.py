# Imports
import cv2
import numpy as np

# This class contains everything needed to run an object detection script based on color.
class ColorDetection:

    # Create Variables
    def __init__(self):
        vid = None

    #This code segment starts up the camera object. This is separated as it should only be run once.
    def startCamera():
        # Create Camera Object
        vid = cv2.VideoCapture(0)
        #vid.set(cv2.CAP_PROP_SATURATION, 65)
        return vid

    # This function does all the heavy lifting and calculations. This is run in the loop.
    def getFrame(vid):
        # Create a frame
        ret, frame = vid.read()

        # Convert RGB Values in frame to HSV
        HSVConvert = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Red Limits: Lower: (0, 50, 50) Upper: (10, 255, 255)
        # Green Limits: Lower: (40, 40, 40) Upper: (80, 255, 255)
        # Blue Limits: Lower: (98, 50, 50) Upper: (139, 255, 255)

        # Set the color mask limits (Default is Green)
        LLimit = (40, 40, 40)
        ULimit = (80, 255, 255)

        # Create Color Mask That isolates blue color from everything else
        colorMask = cv2.inRange(HSVConvert, LLimit, ULimit)

        color = cv2.bitwise_and(frame, frame, mask=colorMask)

        # Create Contour line object
        contours, hier = cv2.findContours(
            colorMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # draw the contours
        output = cv2.drawContours(color, contours, -1, (0, 0, 255), 3)
        
        # Create a mean filter that turns object into a blob: https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html
        kernel = np.ones((5,5),np.float32)/25
        meanFilter = cv2.filter2D(colorMask, -1, kernel)

        # Gather Info about The frame
        M = cv2.moments(meanFilter)
        
        # Take the Centroid Length and Width by doing fancy math: https://learnopencv.com/find-center-of-blob-centroid-using-opencv-cpp-python/ 
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        # You can use this to debug if the centroid calculations are not working.
        # print(str(cX) + " " + str(cY))
        
        # Create Basic Robot Commands
        if cX >= 350:
            turnDir = "Left"
        elif cX <= 250:
            turnDir = "Right"
        else:
            turnDir = "Center"
        
        # Make a point for the centroid and place coordinates
        cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(frame, "Centroid: " + str(cX) + " " + str(cY) + " " + str(turnDir), (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2) # This Is format (:Centroid: :cX: :cY: :turnDir:)

        # Show Frame
        cv2.imshow("frame", frame)

        # Show Isolated Color stuff
        #cv2.imshow("Color Detector", color)
        
        # Show Mean Filter
        #cv2.imshow("Mean Filter", meanFilter)

        # Return the turnDir
        return turnDir

