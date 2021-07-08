
import numpy as np
import imutils
import cv2


# define the lower and upper boundaries of the colors in the HSV color space
lower = {'red': (166, 84, 141),
         'blue': (97, 100, 117),
         'yellow': (23, 59, 119),
         'green': (55, 52, 72),
         'pink': (106, 53, 185)}

upper = {'red': (186, 255, 255),
         'blue': (117, 255, 255),
         'yellow': (54, 255, 255),
         'green': (55, 52, 72),
         'pink': (192, 160, 255)}

# define standard colors for circle around the object
colors = {'red': (0, 0, 255),
          'blue': (255, 0, 0),
          'yellow': (0, 255, 217),
          'green': (0,255,0),
          'pink': (255, 50, 255)}

camera = cv2.VideoCapture(0)

while True:
    # read the video in real time
    _, frame = camera.read()

    # resize the frame
    frame = imutils.resize(frame, width=600)
    # transform in to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # for each color in dictionary check object in frame
    for key, value in upper.items():
        # construct a mask for the color from dictionary`1, then perform
        # a series of dilations and erosions to remove any small
        # blobs left in the mask
        kernel = np.ones((9, 9), np.uint8)
        mask = cv2.inRange(hsv, lower[key], upper[key])
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None

        # only proceed if at least one contour was found
        if len(cnts) > 0:
            contorno = max(cnts, key=cv2.contourArea)
            rect = cv2.minAreaRect(contorno)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            MC = cv2.moments(contorno)
            center = (int(MC["m10"] / MC["m00"]), int(MC["m01"] / MC["m00"]))
            #print(contorno)
            teste = cv2.contourArea(contorno)
            if teste > 1000:
            #[[398 456] [183 441] [198 217] [413 232]]
                cv2.drawContours(frame, [box], 0, colors[key], 2)
                cv2.putText(frame, key + " object", (center), cv2.FONT_HERSHEY_SIMPLEX, 1.0, colors[key], 2)

    # show the frame to our screen
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
