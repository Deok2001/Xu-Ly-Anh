import cv2
import numpy as np
import random
 
I = cv2.imread('Image/TEST.jpg')
cv2.imshow('anh_goc', I)
imgr = I[:, :, 2]
imgg = I[:, :, 1]
imgb = I[:, :, 0]
w = I.shape[1]
h = I.shape[0]
###Lọc trung bình
#Cap phat anh RGB moi
I_avg=np.zeros((h,w,3),dtype='uint8')
I_avg[:,:,2]=cv2.blur(imgr,(3,3))
I_avg[:,:,1]=cv2.blur(imgg,(3,3))
I_avg[:,:,0]=cv2.blur(imgb,(3,3))
cv2.imshow('Loc TB',I_avg)
####lọc median (trung vị)
I_med=np.zeros((h,w,3),dtype='uint8')
I_med[:,:,2]=cv2.medianBlur(imgr,3)
I_med[:,:,1]=cv2.medianBlur(imgg,3)
I_med[:,:,0]=cv2.medianBlur(imgb,3)
cv2.imshow('Loc Median',I_med)
 
###Lọc trọng số
matran_trongso= np.zeros((7,7),dtype='float32')
s=0.0
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=random.random()
        s=s+matran_trongso[i][j]
 
for i in range(7):
    for j in range(7):
        matran_trongso[i][j]=matran_trongso[i][j]/s
 
print(matran_trongso)
I_2 = cv2.filter2D(I,-1,matran_trongso)
cv2.imshow('Loc trong so',I_2)
 
cv2.waitKey()
cv2.destroyAllWindows()
