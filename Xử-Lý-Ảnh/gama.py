import cv2 
import numpy as np 

def hieuchinh_gamma(Igray, gamma = 1.0):
  w=Igray.shape[1]
  h=Igray.shape[0]

  Igray_new=np.zeros((h,w),dtype='uint8')
  for i in range(h):
    for j in range(w):
      g_f=float(Igray[i][j])/255.0
      g_f_new=np.power(g_f, gamma)
      g_new=int(g_f_new*255.0)
      Igray_new[i][j]=g_new
  return Igray_new

I=cv2.imread('Image/dark.jpg')
cv2.imshow('goc',I)
Ir=I[:,:,2]
Ig=I[:,:,1]
Ib=I[:,:,0]

w=I.shape[1]
h=I.shape[0]
I_new=np.zeros((h,w,3),dtype='uint8')
gamma=0.5
cv2.imshow('gama',I_new)

cv2.waitKey(0)
cv2.destroyAllWindows()