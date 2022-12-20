import cv2 as cv
import imutils as im
from Functions import humanDetect as hD
from Functions import showImage as sI

def load(path):
    image = cv.imread(path)

    dimension = image.shape

    sI.show(image)

    image = im.resize(image, width=min(612, image.shape[1]))

    result_image = hD.detect(image)

    result_image = im.resize(result_image, width=max(dimension[1], image.shape[1]))

    sI.show(result_image)

