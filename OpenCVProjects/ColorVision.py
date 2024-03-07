import cv2
import numpy as np

# Create Camera Object
vid = cv2.VideoCapture(0)

while True:
    # Create a frame
    ret, frame = vid.read()

    # Convert RGB Values in frame to HSV
    HSVConvert = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Set the color mask limits
    LLimit = (40, 40, 40)
    ULimit = (80, 255, 255)

    # Create Color Mask That isolates blue color from everything else
    colorMask = cv2.inRange(HSVConvert, LLimit, ULimit)

    color = cv2.bitwise_and(frame, frame, mask=colorMask)

    # Show Frame
    cv2.imshow("frame", frame)

    # Show Isolated Color stuff
    cv2.imshow("ColorDetector", color)

    # Quit with "Q" Button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kill windows after finished
vid.release()

# Boom
cv2.destroyAllWindows()

