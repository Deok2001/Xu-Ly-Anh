
# 1.  Đọc và hiển thị ảnh I.
import cv2
import numpy as np
I = cv2.imread('Image/I04.jpg')
cv2.imshow("Anh goc", I)

# 2. Chuyển ảnh mầu I sang ảnh đa cấp xám (grayscale) theo công thức (0.39,0.5,0.11), được ma trận ảnh Ig. Hiển thị ảnh Ig. Xác định mức xám lớn nhất của ảnh Ig.
I_red = I[:,:,2]
I_green = I[:,:,1]
I_blue = I[:,:,0]
def anhXam(img):
    imageHeight = img.shape[0]
    imageWidth = img.shape[1]
    Igray = np.empty([imageHeight, imageWidth], dtype = np.uint8) #uint8 số nguyên 8bit ko dấu
    for i in range(imageHeight):
        for j in range(imageWidth):
            Igray[i][j] = int(img[i][j][0]*0.39 + img[i][j][1]*0.5 + img[i][j][2]*0.11)
    return Igray
Igray = anhXam(I)
cv2.imshow('Anh xam theo ham chuyen', Igray)
a= Igray.max()
print('Max cua Igray', a)
# 3. Lấy biên của ảnh Ig theo phương pháp Canny được ảnh biên Ie là ảnh nhị phân nền đen. Kiểm tra pixel có tọa độ dòng y=160, cột x=326 có là điểm biên của ảnh Ig theo phép dò biên Canny không?
ICanny = cv2.Canny(image=I,threshold1=100, threshold2=200) # tìm biên theo Canny
cv2.imshow('Anh ICanny', ICanny)

(h, w, d) = I.shape
B, G, R = cv2.split(I)
 
if(ICanny[326][160]==255):
    print("Tọa độ [326,160] là điểm biên của ảnh")
else:
    print("Tọa độ [326,160] không phải là điểm biên của ảnh!")

     #3.1. Xác định ma trận  theo hướng y và theo hướng x của Ig sử dụng toán tử Sobel và hiển thị 2 ma trận kết quả. 

sobelx = cv2.Sobel(I_blue,ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)  # tìm biên sobel đạo hàm theo x
sobely = cv2.Sobel(I_blue,cv2.CV_64F,0,1,ksize=5)  #  tìm biên sobel đạo hàm the y
cv2.imshow('Sobelx',sobelx)
cv2.imshow('Sobely',sobelx)
print(sobelx)
print(sobely)
# 4.  Nhị phân ảnh Ig theo ngưỡng Otsu được ảnh nhị phân nền đen được ảnh Ib. Hiển thị ảnh Ib.
ret, Ib = cv2.threshold(Igray, 180, 255, cv2.THRESH_OTSU)
cv2.imshow("Anh nhi phan nguong Otsu", Ib)
# 5. Xác định các đường contour của ảnh Ib, tìm giá trị max_cv là chu vi lớn nhấgradientt trong các contour trên. Vẽ các contours có chu vi lớn nhất lên ảnh gốc I với mầu bgr = (0,0,255). Hiển thị ảnh I.
I_copy = I.copy()
contours, hierarchy = cv2.findContours(Ib, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(I_copy, contours, -1, (0,255,0), 3) #vẽ trên ảnh gốc
cv2.imshow("Contour",I_copy)

i = 0.0
for j in contours:
    chuvi = cv2.arcLength(j, True)
    if(chuvi > i):
        i = chuvi
print("chu vi lon nhat cua cac contours la :",i)
for contour in contours:
  if cv2.contourArea(contour) == i:
      cv2.drawContours(I, [contour], -1, (0,0,255), 3)
cv2.imshow('Anh goc moi',I)
cv2.waitKey()
cv2.destroyAllWindows()