import cv2
import numpy as np
import matplotlib.pyplot as plt
#1 Đọc ảnh mầu hat1.png vào biến ma trận I. Hiển thị ảnh I.
I = cv2.imread('Image/hat1.PNG')
cv2.imshow('Anh goc',I)
#2 Chuyển ảnh sang biểu diễn HSV được ma trận Ihsv. Hiển thị kênh V của Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh V', Ihsv[:,:,2])
#Xác định giá trị mức sáng lớn nhất của kênh H của ảnh Ihsv.
print("Muc xam tuyet doi:",np.max(Ihsv[:,:,0]))
#3 Vẽ histogram của kênh S của ảnh Ihsv.
Is = cv2.calcHist([Ihsv[:,:,1]], [0], None, [256], [0, 256])
plt.plot(Is)
plt.show()
#4 Làm trơn ảnh kênh S của Ihsv theo bộ lọc median, kích thước cửa sổ lân cận
#là 5x5 được ảnh Is. Hiển thị ảnh Is.
I_med = cv2.medianBlur(Ihsv[:,:,1],5)
cv2.imshow('Loc median S',I_med)
#5 Xác định đường contour có chu vi lớn nhất của ảnh Ib. Vẽ đường contour trên ảnh gốc I. Hiển thị ảnh I.
img_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)
ret, Ib = cv2.threshold(img_gray, 180, 255, cv2.THRESH_OTSU)
img_copy = I.copy()
contours, hierarchy = cv2.findContours(
    Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#tinh chu vi contour
i=0.0
for j in contours:
    chuvi = cv2.arcLength(j, True)
    if(chuvi>i):
        i=chuvi
print("chu vi lon nhat cua cac contours la :",i)
for contour in contours:
  if cv2.arcLength(contour,True) == i:
      cv2.drawContours(img_copy, [contour], -1, (0,0,255), 3)
     
cv2.imshow('Contours',img_copy)
cv2.waitKey(0)
