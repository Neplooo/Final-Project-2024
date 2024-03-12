import cv2
import numpy as np

# Create Camera Object
vid = cv2.VideoCapture(0)
#vid.set(cv2.CAP_PROP_SATURATION, 65)

while True:
    # Create a frame
    ret, frame = vid.read()

    # Convert RGB Values in frame to HSV
    HSVConvert = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red Limits: Lower: (0, 50, 50) Upper: (10, 255, 255)
    # Green Limits: Lower: (40, 40, 40) Upper: (80, 255, 255)
    # Blue Limits: Lower: (98, 50, 50) Upper: (139, 255, 255)

    # Set the color mask limits
    LLimit = (40, 40, 40)
    ULimit = (80, 255, 255)

    # Create Color Mask That isolates blue color from everything else
    colorMask = cv2.inRange(HSVConvert, LLimit, ULimit)

    color = cv2.bitwise_and(frame, frame, mask=colorMask)

    contours, hier = cv2.findContours(
        colorMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    output = cv2.drawContours(frame, contours, -1, (0, 0, 255), 3)

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

