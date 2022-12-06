import cv2 as cv

HOGCV = cv.HOGDescriptor()
HOGCV.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())


def detect(frame):
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8), scale=1.03)

    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, f'person {person}', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1

    cv.putText(frame, f'Total Persons : {person - 1}', (40, 70), cv.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)

    return frame
