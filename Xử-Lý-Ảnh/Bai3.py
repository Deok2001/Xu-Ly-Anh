import cv2 
import numpy 
import matplotlib 

I = cv2.imread('Image/TEST.jpg')
cv2.imshow('image', I)


#Hiển thi kích thước ảnh, số kênh
print('Chiều cao:',I.shape[0])
print('Chiều rộng:',I.shape[1])
print('Kênh ảnh:',I.shape[2])

#Hiển thị kênh G của ảnh 
cv2.imshow('Kenh G',I[:,:,1])

#Resize image = 1/2
scale_percent = 50 # percent of original size
width = int(I.shape[1] * scale_percent / 100)
height = int(I.shape[0] * scale_percent / 100)
dim = (width, height)
  
resized = cv2.resize(I, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)
 
cv2.imshow("Resized image", resized)

#Chuyển ảnh màu sang ảnh xám 
Ig2=cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image',Ig2)

#Tách lấy kênh R của ảnh. Chuyển ảnh kênh R sang ảnh trắng đen với ngưỡng 90
imgR = I[:,:,2]
cv2.threshold(imgR,90,255,cv2.THRESH_BINARY)
cv2.imshow('Image 7',imgR)

cv2.waitKey(0)
cv2.destroyAllWindows()
