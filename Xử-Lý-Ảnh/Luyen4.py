import cv2
import numpy as np

#1
I = cv2.imread('Image/anh5.jpg')
cv2.imshow("Anh goc", I)

#2
w = int(I.shape[1] * 2)
h = int(I.shape[0] * 2)
dim = (w,h)
I_resize = cv2.resize(I, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Anh da thay doi", I_resize)

#3
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
Is = Ihsv[:,:, 1]
Is = cv2.blur(Is, (5,5))
cv2.imshow('anh sau khi loc trung binh cong', Is)

# 4
thresh, Ib = cv2.threshold(Is, 90, 255, cv2.THRESH_OTSU)

I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1 , (0,255,0), 2)
cv2.imshow('Anh vien cua anh I',I_copy)

max_arc = 0.0
for cnt in contours:
    if cv2.arcLength(cnt,True) > max_arc:
        max_arc = cv2.arcLength(cnt,True)
print(max_arc)

#5
def correction_gamma(I, gamma=1.0):
    h = I.shape[0]
    w = I.shape[1]

    I_new=np.zeros((h,w),dtype='uint8')
    for i in range(h):
        for j in range(w):
            g_f=float(I[i][j])/255.0
            g_f_new=np.power(g_f, gamma)
            g_new=int(g_f_new*255.0)
            I_new[i][j]=g_new
    return I_new
Ihsv[:,:,2] = correction_gamma(Ihsv[:,:,2], 0.5)
I = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow('anh goc ban dau', I)

cv2.waitKey(0)
cv2.destroyAllWindows() 