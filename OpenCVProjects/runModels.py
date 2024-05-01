# NOTE: Make sure you have a Green Object in front of the camera before you start the program.

from ColorVision import *
import cv2

video = ColorDetection.startCamera()

while True:
    ColorDetection.getFrame(vid=video)

    # Quit with "Q" Button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Kill windows after finished
ColorDetection.vid.release()

# Boom (Shaka Laka)
cv2.destroyAllWindows()