import cv2
# Cau 1
# đọc và hiển thị ảnh
I = cv2.imread('Image/the_cancuoc_congdan.jpg')
cv2.imshow('Anh goc', I)
# hiển thị kênh R
cv2.imshow('Kenh red', I[:,:,2])
# Cau 2
# Chuyển ảnh sang ảnh grayscale
import numpy as np
def anhXam(img):
    imageHeight = img.shape[0]
    imageWidth = img.shape[1]
    Igray = np.empty([imageHeight, imageWidth], dtype = np.uint8) #uint8 số nguyên 8bit ko dấu
    for i in range(imageHeight):
        for j in range(imageWidth):
            Igray[i][j] = int(img[i][j][0]*0.2126 + img[i][j][1]*0.7152 + img[i][j][2]*0.0722)
    return Igray
Igray = anhXam(I)
cv2.imshow('Anh xam theo ham chuyen', Igray)
# Cau 3
# Chuyển ảnh Ig sang ảnh nhị phân Ib với ngưỡng quyết định nhị phân 90. Hiển thị ảnh nhị phân Ib.
(nguong, Ib) = cv2.threshold(Igray, 90, 255, cv2.THRESH_BINARY)
cv2.imshow('anh nhi phan nguong 90', Ib)
# Cau 4
# Làm trơn ảnh Ig theo bộ lọc median với lân cận cửa sổ kích thước 5x5 thu được ảnh Im. Hiển thị ảnh kết quả Im.
h=Igray.shape[0]
w=Igray.shape[1]
####lọc median (trung vị) 
I_med=np.zeros((h,w,3),dtype='uint8')
I_med=cv2.medianBlur(Igray,5)
cv2.imshow('Loc median', I_med)

cv2.waitKey()
cv2.destroyAllWindows()