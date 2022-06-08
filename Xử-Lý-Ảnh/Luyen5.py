from itertools import count
import cv2 
# Đọc ảnh  I.
# 1. Hiển thị
# ảnh I.
I = cv2.imread('Image/anh5.jpg')
cv2.imshow('Original', I)

# 2. Chuyển ảnh mầu I sang ảnh đa cấp xám với thành phần mầu (r,g,b) là  (0.39,0.5,0.11), được ma
# trận ảnh Ig. Hiển thị Ig. Tính mức xám trung bình của Ig.
def cvtGray(I):
    grayColor = .39 * I[:, :, 2] + .5 * I[:, :, 1] + .11 * I[:, :, 0]
    grayColor = grayColor.astype(dtype='uint8')

    return grayColor

Ig = cvtGray(I)
cv2.imshow('Gray Img', Ig)
print('Mean Gray : ', Ig.mean())

# 3. Chuyển  I sang dạng HSV được ảnh Ihsv. Xác định mức xám lớn nhất của
# kênh S của Ihsv.
Ihsv = cv2.cvtColor(I, cv2.COLOR_BGR2HSV)
Ihsv_s = Ihsv[:, :, 1]
print('Max Gray S channel HSV img : ', Ihsv_s.max())

# 4. Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib.
# Hiển thị ảnh Ib.
thresh, Ib = cv2.threshold(Ig, 180, 255, cv2.THRESH_OTSU)
cv2.imshow('Binary Img', Ib)

# 5. Xác định  contour của Ib, tìm giá trị max của contour có chu vi lớn nhất. Vẽ các contours có chu vi > max/5 lên ảnh gốc I với mầu (255,0,255). Hiển thị.
I_copy = I.copy()
contours, hie = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Ib contours : ', contours)
cv2.drawContours(I_copy, contours, -1, (0, 0, 255), 2)

I_copy = I.copy()
max_cv = 0.0

for cnt in contours:
    if max_cv < cv2.arcLength(cnt, True):
        max_cv = cv2.arcLength(cnt, True)
print('Max CV : ',  max_cv)

for cnt in contours:
    if cv2.arcLength(cnt, True) > max_cv/5:
        cv2.drawContours(I_copy, cnt, -1, (255,0,255), 2)
cv2.imshow('Draw Contours', I_copy)

cv2.waitKey()