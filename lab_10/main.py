import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\AppData\Local\Tesseract-OCR\tesseract'

path_img1 = "Images/image1.png"

img = cv2.imread(path_img1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


converted_img = cv2.threshold(cv2.GaussianBlur(img, (5, 5), 0), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


text1 = pytesseract.image_to_string(path_img1)

print(text1)