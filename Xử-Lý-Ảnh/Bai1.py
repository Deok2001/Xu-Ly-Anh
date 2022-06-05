import cv2 
import numpy 
import matplotlib 

I = cv2.imread('Image/TEST.jpg')
cv2.imshow('image', I)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Hiển thi kích thước ảnh, số kênh
print('Chiều cao:',I.shape[0])
print('Chiều rộng:',I.shape[1])
print('Kênh ảnh:',I.shape[2])

#Hiển thị từng kênh ảnh
cv2.imshow('Kenh red',I[:,:,2])
cv2.imshow('Kenh green',I[:,:,1])
cv2.imshow('Kenh blue',I[:,:,0])

cv2.waitKey()