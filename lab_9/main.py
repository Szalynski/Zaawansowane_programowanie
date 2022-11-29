import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\student\AppData\Local\Tesseract-OCR\tesseract'

path_img1 = "Images/image1.png"
path_img2 = "Images/image2.jpg"
path_img3 = "Images/image3.jpg"
path_img4 = "Images/image4.jpg"
path_img5 = "Images/image5.jpg"

text1 = pytesseract.image_to_string(path_img1)
text2 = pytesseract.image_to_string(path_img2)
text3 = pytesseract.image_to_string(path_img3)
text4 = pytesseract.image_to_string(path_img4)
text5 = pytesseract.image_to_string(path_img5)

print(text1+"\n"+text2+"\n"+text3+"\n"+text4+"\n"+text5)