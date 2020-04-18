import cv2
import os

cam = cv2.VideoCapture(0)
currentframe = 0

while (True):
    ret, frame = cam.read()
    name = './images/withoutmaskImage/wmimage' + str(currentframe) + '.jpg'
    print('Creating...' + name)
    cv2.imwrite(name, frame)
    currentframe += 1
    if currentframe>200:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()