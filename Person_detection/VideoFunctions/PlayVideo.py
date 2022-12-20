import cv2 as cv
import numpy as np

def load(name3):
    hog = cv.HOGDescriptor()
    hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

    cv.startWindowThread()
    cap = cv.VideoCapture(name3)

    while (True):
        ret, frame = cap.read()
        if (ret == False):
            break
        frame = cv.resize(frame, (640, 480))
        boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        person = 1
        for (xA, yA, xB, yB) in boxes:
            cv.rectangle(frame, (xA, yA), (xB, yB),
                         (0, 255, 0), 2)
            person += 1

        cv.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)

        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(1)