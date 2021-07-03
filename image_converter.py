import img2pdf
from PIL import Image
import os
i=1
lists = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,23,24,25,26,28,30,31,32,33,41,42,43,44,45,46,47,48,49,50]
for x in lists:
    img_path = "D:/sem-4/MF-219/QFD/"+str(x)+".jpg"
    pdf_path = "D:/sem-4/MF-219/file"+str(i)+".pdf"

    image = Image.open(img_path)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(pdf_path, "wb")
    file.write(pdf_bytes)
    file.close()
    print("Successfully made pdf of file"+str(i)+".pdf")
    i+=1
