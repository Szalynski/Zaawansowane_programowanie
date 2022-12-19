import cv2 as cv
import numpy as np
def load(name3):
    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

    cv.startWindowThread()
    cap = cv.VideoCapture(name3)

    while(True):
        ret, frame = cap.read()
        if(ret == False):
            break
        frame = cv.resize(frame, (640, 480))
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            cv.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)

    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(1)