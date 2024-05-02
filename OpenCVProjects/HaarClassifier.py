# Import Requisites
import cv2
import numpy

# Create Camera Object
vid = cv2.VideoCapture(0)

while(True):
    # Create a frame
    ret, frame = vid.read()

    # Convert Frame to Grayscale
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Create Haar Classifier Object (From https://github.com/opencv/opencv/tree/4.x/data/haarcascades)
    haarCascade = cv2.CascadeClassifier("C:/Users/Albert.Mathisz/PycharmProjects/OpenCVTest/haarcascade_frontalface_default.xml")

    # Apply Haar Classifier on Grayscale frame
    rectFaces = haarCascade.detectMultiScale(grayFrame, 1.1, 9)

    # Iterate through the faces in the frame and apply s q u a r e
    for (x, y, w, h) in rectFaces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Show Frame
    cv2.imshow("frame", frame)

    # Quit with "Q" Button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kill windows after finished
vid.release()

cv2.destroyAllWindows()
