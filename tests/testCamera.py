# NOTE: If test passes: Camera is plugged in. If Test fails, Camera is not plugged in.

# Import Stuff
import os, sys
import unittest
import cv2
import numpy as np

#Find The Relative Path for The ColorVision.py file
scriptDir = os.path.dirname(__file__)
moduleDir = os.path.join(scriptDir, "..", "OpenCVProjects",)
sys.path.append(moduleDir)

# Import the ColorVision Code
from ColorVision import ColorDetection

# Camera Test will check to see if camera is plugged in
class TestCamera(unittest.TestCase):

    def test_cam(self):
        self.camCheck = ColorDetection()
        cam = cv2.VideoCapture(0)
        self.assertTrue(cam.isOpened())


unittest.main(argv=[''], verbosity=2, exit=False)
