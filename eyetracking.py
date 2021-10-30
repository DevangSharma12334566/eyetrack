import numpy as np
import cv2
import argparse
import os, sys, inspect

cmd_subfolder = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "..", "..", "Image_Lib")))
if cmd_subfolder not in sys.path:
    sys.path.insert(0, cmd_subfolder)

import image_utils as utils
import EyeTrackingLib as tracker

ap = argparse.ArgumentParser("Finds pupil location in eyes")
ap.add_argument("-i", "--image", required=True, help="Path to image file")
ap.add_argument("-m", "--mode", required=False, help="Process after detecting face Y/N. Default = Y")
args = vars(ap.parse_args())

face_cascade = cv2.CascadeClassifier('Image_Lib/Face_Data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('Image_Lib/Face_Data/haarcascade_eye.xml')
if not args.get("mode", None):
    detect_face = True
else:
    detect_face = False

image = cv2.imread(args["image"])
print image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
tracker.showImage = True

face_box = None
faces = face_cascade.detectMultiScale(gray, 1.1, 3)
if len(faces) > 0:
    face_box = max(faces, key=lambda item: item[2] * item[3])
