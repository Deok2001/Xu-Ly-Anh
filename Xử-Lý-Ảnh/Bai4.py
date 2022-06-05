import cv2 
import numpy

I = cv2.imread('Image/CMTND01.jpg')
cv2.imshow('image', I)
#Hiển thị giá trị pixel điểm ảnh tại tọa độ y=40 (dòng), x=15 (cột).
print('Img point : ', I[40, 15])

#2. 
Ig2=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
ret, bina1 = cv2.threshold(Ig2,90,255,cv2.THRESH_BINARY)
cv2.imshow("Binary 1 BINARY : ",bina1)
ret, bina2 = cv2.threshold(Ig2,90,255,cv2.THRESH_OTSU)
cv2.imshow("Binary 2 OTSU : ",bina2)
#3
img3_5 = cv2.resize(I,(500,300))
cv2.imshow("300x500 : ",img3_5)
cv2.imwrite("CMND01_300_500.png",I)
#4
print(numpy.min(I[:,:,2]))
print(numpy.max(I[:,:,2]))


cv2.waitKey(0)
cv2.destroyAllWindows()
