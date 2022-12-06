import cv2 as cv
import imutils as im
from Functions import humanDetect as hD
from Functions import showImage as sI

def load(path):
    image = cv.imread(path)

    image = im.resize(image, width=min(2000, image.shape[1]))

    result_image = hD.detect(image)

    sI.show(result_image)

