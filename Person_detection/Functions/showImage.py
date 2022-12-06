import cv2 as cv


def show(name: str) -> None:
    cv.imshow("Image", name)
    cv.waitKey(0)

    cv.destroyAllWindows()
