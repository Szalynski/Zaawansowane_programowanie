import cv2 as cv

HOGCV = cv.HOGDescriptor()
HOGCV.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, f'person {person}', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        person += 1

    cv.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)

    return frame
