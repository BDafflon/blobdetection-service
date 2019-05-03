import cv2
import numpy as np
from flask import Flask

app = Flask(__name__)

def captureFrame(cap):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    return gray

def blob(img):
    params = cv2.SimpleBlobDetector_Params()
 
    # Change thresholds
    params.minThreshold = 1;
    params.maxThreshold = 100;

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 15

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.01

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector_create(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
   

    # Detect blobs.
    keypoints = detector.detect(img)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    return im_with_keypoints

def blobCounter(img):
    params = cv2.SimpleBlobDetector_Params()
 
    # Change thresholds
    params.minThreshold = 1;
    params.maxThreshold = 100;

    # Filter by Area.
    params.filterByArea = True
    params.minArea = 15

    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.01

    # Filter by Convexity
    params.filterByConvexity = False
    params.minConvexity = 0.87

    # Filter by Inertia
    params.filterByInertia = False
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector_create(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)
    
   

    # Detect blobs.
    keypoints = detector.detect(img)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    # Show keypoints
    return len(keypoints)


def save():
    return

def init():
    cap = cv2.VideoCapture(0)
    return cap



@app.route('/start')
def startCam():
    cap = cv2.VideoCapture(0)
    cap = init()
    return 'start'

@app.route('/captureblob')
def capture():
    cap = cv2.VideoCapture(0)
    gray = captureFrame(cap)
    blob(gray)
    save()
    return 'end'

@app.route('/blobCounter')
def blobcounter():
    cap = init()
    # Capture frame-by-frame
    gray = captureFrame(cap)


    img = blob(gray)
    nbBlob = blobCounter(gray)

    print(nbBlob)
    
    return str(nbBlob)

if __name__ == '__main__':
     app.run(port='5002')
 
