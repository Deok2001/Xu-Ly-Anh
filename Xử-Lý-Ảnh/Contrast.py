import cv2 
import numpy as np
import matplotlib.pyplot as plt

def tinh_hist(Ig):
    a=np.zeros(256,dtype='int')
    h=Ig.shape[0]
    w=Ig.shape[1]
    for i in range(h):
        for j in range(w):
             g=Ig[i][j]
             a[g]=a[g]+1
    return a

print('Kênh B')
I=cv2.imread('Image/I04.jpg')
IB=I[:,:,0]
hB=tinh_hist(IB)

plt.plot(hB)
plt.show()

print('Sử dụng thư viện vẽ hist kênh B')
hB_ = cv2.calcHist([IB],[0],None,[256],[0,256])
plt.plot(hB_)
plt.show()

I_new=I.copy()
I_new[:,:,0]= cv2.equalizeHist(I[:,:,0])
cv2.imshow('Can bang kenh B',

I_new[:,:,0])
I_new[:,:,1]= cv2.equalizeHist(I[:,:,1])
cv2.imshow('Can bang kenh G', I_new[:,:,1])
I_new[:,:,2]= cv2.equalizeHist(I[:,:,2])
cv2.imshow('Can bang kenh R', I_new[:,:,2])
#gọi tiếp hàm 

cv2.imshow('Anh RGB sau khi can bang',I_new)
cv2.waitKey()