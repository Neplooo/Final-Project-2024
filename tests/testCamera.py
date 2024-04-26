# NOTE: DO NOT USE, TEST ALGORITHM IS STILL BROKEN

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

#result = str(ColorDetection.startCamera())
#print(result)
#formatResult = result.join(line.strip() for line in result.splitlines())
#print(formatResult)

# CAMERA TEST STILL BROKEN
class TestCamera(unittest.TestCase):
    
    def test_cam(self):
        self.camCheck = ColorDetection()
        cam = self.camCheck.startCamera
        self.assertTrue()

unittest.main(argv=[''], verbosity=2, exit=False)
