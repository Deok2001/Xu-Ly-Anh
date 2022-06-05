import cv2
from cv2 import cvtColor
import numpy as np

I = cv2.imread('Image/Coins.jpg')
# cv2.imshow('Anh goc', I)

I_gray = cvtColor(I, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Anh gray', I_gray)

I_blur = cv2.blur(I_gray,(3,3))
# cv2.imshow('Anh blur', I_blur)

###Tìm biên theo SOBEL
sobelx = cv2.Sobel(I,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=1)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I,cv2.CV_64F,0,1,ksize=1)  #  tìm biên sobel đạo hàm the y
# cv2.imshow('anh sobelx', sobelx)
# cv2.imshow('anh sobely', sobely)

img = cv2.GaussianBlur(I_gray, (3,3), 0) #lọc ảnh Gaussian 
# cv2.imshow('loc gaussian', img)

###Tìm biên theo Laplacian và Canny
laplacian = cv2.Laplacian(img, cv2.CV_64F) #tìm biên theo laplacian
ICanny = cv2.Canny(image=I,threshold1=100, threshold2=200) # tìm biên theo Canny
cv2.imshow('Anh laplacian', laplacian)
cv2.imshow('Anh ICanny', ICanny)

# Lấy biên Sobel trung bình theo cả x và y
img_gaussion = cv2.GaussianBlur(I_gray, (5,5), 0)
img_sobelx = cv2.Sobel(img_gaussion, cv2.CV_64F, dx=1,dy=0, ksize=1)
img_sobely = cv2.Sobel(img_gaussion, cv2.CV_64F,0,1,ksize=1)
cv2.imshow('Anh img_gaussion', img_gaussion)

img_sobelx = np.uint8(np.absolute(img_sobelx))
img_sobely = np.uint8(np.absolute(img_sobely))
cv2.imshow('Anh img_sobelx', img_sobelx)
cv2.imshow('Anh img_sobely', img_sobely)

img_sobel = (img_sobelx + img_sobely)/2
for i in range(img_sobel.shape[0]):
    for j in range(img_sobel.shape[1]):
        if img_sobel[i][j] < 25:
            img_sobel[i][j] = 0
        else:
            img_sobel[i][j] = 255

cv2.imshow('anh sobel',img_sobel)

cv2.waitKey(0)