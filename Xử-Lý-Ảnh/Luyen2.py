# Bài luyện số 2: - 20' 
# 1. hiện thị ảnh anh2.jpg gán vào I 
import cv2
import numpy as np
I =cv2.imread('Image/anh2.jpg')
cv2.imshow("Anh goc",I)
# 2. Viết hàm chuyển I thành ảnh đa cấp xám theo tỷ lệ (0.39,0.5,0.11), được ma trận ảnh Ig. Xác định mức xám lớn nhất và mức xám trung bình của ảnh Ig.
I_red = I[:,:,2]
I_green = I[:,:,1]
I_blue = I[:,:,0]
def toGray(I): 
    Ig=0.39*I_red+0.5*I_green+0.11*I_blue 
    Ig=Ig.astype(dtype='uint8') 
    return Ig 
I_gray = toGray(I) 
cv2.imshow('Anh xam I_gray',I_gray)
a= I_gray.max()
print('Max cua I_gray',a)
# 3. Xác định ma trận gradient theo hướng y và theo hướng x của Ig sử dụng toán tử Sobel và hiển thị 2 ma trận kết quả.
sobelx = cv2.Sobel(I_blue,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I_blue,cv2.CV_64F,0,1,ksize=5)  #  tìm biên sobel đạo hàm the y
cv2.imshow('Sobelx',sobelx)
cv2.imshow('Sobely',sobelx)
print(sobelx)
print(sobely)
# 4. Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Hiển thị các độ xám của của cửa sổ lân cận 3x3 của pixel có tọa độ dòng y=78, cột x=23 của ảnh Ig.

# I[77,22]   I[77,23]  I[77,24] 
# I[78,22]   I[78,23]  I[78,24] 
# I[79,22]   I[79,23]  I[79,24] 
Ie = cv2.Canny(image=I[:,:,1], threshold1=100,threshold2=200)  # tìm biên theo Canny
cv2.imshow('Ie', Ie)
I_gray = cv2.medianBlur(I_gray,3)
cv2.imshow('Gray', I_gray)
print("Mức xám y=78 x=23:", I_gray[78][23])

# 5. Nhị phân ảnh Ig với ngưỡng 150 được ảnh nhị phân nền đen Ib. Chuyển thành ảnh nền đen. Xác định các đường
# contour của ảnh Ib. Loại các countour bé. Vẽ các đường contour trên lên ảnh gốc I.
ret, Ib = cv2.threshold(I_gray, 150, 255, cv2.THRESH_OTSU)
img_copy = I.copy()
Ib=255-Ib
contours, hierarchy = cv2.findContours(
Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
        if cv2.contourArea(contour) > 1600:
            cv2.drawContours(img_copy, [contour], -1, (0,0, 255), 3)
cv2.imshow('Anh Contours', img_copy)
cv2.waitKey()
cv2.destroyAllWindows()