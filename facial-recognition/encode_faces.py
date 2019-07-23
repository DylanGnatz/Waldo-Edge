#Based on https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/ by Adrian Rosebrock
# import the necessary packages
from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os
import dlib
import contains_util

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dataset", required=True,
    help="path to input directory of faces + images")
ap.add_argument("-e", "--encodings", required=True,
    help="path to serialized db of facial encodings")
ap.add_argument("-d", "--detection-method", type=str, default="hog",
    help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# grab the paths to the input images in our dataset
print("[INFO] quantifying faces...")
data = pickle.loads(open(args["encodings"], "rb").read()) if os.path.exists(args["encodings"]) else {"details":[], "encodings": []}
imagePaths = list(paths.list_images(args["dataset"]))
 
# initialize the list of known encodings and known names
knownEncodings = []
knownNames = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    imgname = imagePath.split(os.path.sep)[-1]
    if not contains_util.list_dicts_contains(data["details"], "imageName", imgname):
        # extract the person name from the image path
        print("[INFO] processing image {}/{}".format(i + 1,
            len(imagePaths)))
        splitname = imgname.split(".")[0]
        splitname = splitname.split("-")
        details = {"imageName": imgname, "personID": splitname[0], "personName": splitname[1], "fileName": splitname[2]}
        knownNames.append(details)


        # load the input image and convert it from BGR (OpenCV ordering)
        # to dlib ordering (RGB)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input image
        boxes = face_recognition.face_locations(rgb,
            model=args["detection_method"]) 
    
        # compute the facial embedding for the face
        encodings = face_recognition.face_encodings(rgb, boxes)
    
        # loop over the encodings
        for encoding in encodings:
            # add each encoding + name to our set of known names and
            # encodings
            knownEncodings.append(encoding)
            #knownNames.append(name)

# dump the facial encodings + names to disk
print("[INFO] serializing encodings...")
newData = {"encodings": knownEncodings, "details": knownNames}
data["encodings"].extend(newData["encodings"])
data["details"].extend(newData["details"])





f = open(args["encodings"], "wb")
f.truncate(0)
f.write(pickle.dumps(data))
f.close()

