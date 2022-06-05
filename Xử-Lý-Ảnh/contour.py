# 1. Đọc và hiển thị ảnh Coins.jpg
import cv2
import numpy as np
I = cv2.imread('Image/tao.jpg')
cv2.imshow("Anh goc", I)
#2. Chuyển ảnh I thành ảnh grayscale I_gray
Igray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow("Anh grayscale",Igray)
# 3. Chuyển từ ảnh Igray sang ảnh nhị phân I_bina
# - C1: Theo ngưỡng nhị phân 
thresh, I_bina = cv2.threshold(Igray, 180, 255, cv2.THRESH_BINARY)
cv2.imshow('Anh nhi phan nguong 90', I_bina)
#Tự viết hàm nhị phân ảnh
# def change_image(I,thresh):
#    h,w = I.shape
#    Ib = np.zeros((h,w))
#    for t in range(h):
#     for t1 in range(w):
#        if I[t][t1] < thresh:
#            Ib[t][t1]=0
#        else: Ib[t][t1] = 255
#     return Ib
# I_bina = change_image(Igray,120)
# cv2.imshow('anh nhi phan',I_bina)

#- C2: Theo ngưỡngTHRESH_OTSU / ADAPTIVE_THRESH_GAUSSIAN_C / ADAPTIVE_THRESH_MEAN_C
# Igray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
# ret, I_binary1 = cv2.threshold(Igray, 90, 255, cv2.THRESH_OTSU)
# cv2.imshow('anh nhi phan THRESH_OTSU',I_binary1)
# thresh, I_binary2=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
# cv2.imshow('anh nhi phan ADAPTIVE_THRESH_GAUSSIAN_',I_binary2)

# thresh, I_binary3=cv2.threshold(Igray,90,255, cv2.ADAPTIVE_THRESH_MEAN_C)
# cv2.imshow('anh nhi phan ADAPTIVE_THRESH_MEAN_C',I_binary3)

#4. Tìm  contour của ảnh I_bina
I_copy = I.copy()
contours, hierarchy = cv2.findContours(I_bina, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy   , contours, -1, (0,255,0), 3) #vẽ trên ảnh gốc
cv2.imshow('anh contour',I_copy)

#5. Loại bỏ các contour bé
#C1: 
for contour in contours:
  if cv2.contourArea(contour) > 200:
      cv2.drawContours(I_copy, [contour], -1, (0,255,0), 3)
cv2.imshow('contours',I_copy)
#C2: 
Icc = I.copy()
max_area=0.0
for cnt in contours:
    if max_area < cv2.contourArea(cnt):
        max_area=cv2.contourArea(cnt)
for cnt in contours:
    if cv2.contourArea(cnt) > max_area/2:
        cv2.drawContours(Icc,[cnt],-1,(0,0,255),2)
cv2.imshow("bo cac contour qua nho",Icc)

cv2.waitKey()
cv2.destroyAllWindows()