import cv2
import numpy as np
import pandas as pd
# ĐỌC ẢNH 
# Sử dụng bút bi nét đậm, viết tay chỉ 1 chữ số (từ 0 đến 9), 
# khoanh vùng chữ số được 1 ảnh, sử dụng ví dụ Paint brush, 
# chuẩn hóa ảnh thành ảnh gray, kích thước 28x28(cao 28, rộng 28), ghi lại được 1 ảnh vidu.jpg. 
# 1. Sử dụng OpenCV đọc ảnh vidu.jpg được ma trận ảnh I. 
I = cv2.imread('Image/tao.jpg')
# cv2.imshow('Original', I)
Ig = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)
Iresize = cv2.resize(Ig, (28, 28), interpolation=cv2.INTER_AREA)
cv2.imwrite('Vidu.jpg', Iresize)
# cv2.imshow('Vidu', Iresize)

Inew = cv2.imread('Vidu.jpg')
IgNew = cv2.cvtColor(Inew, cv2.COLOR_RGB2GRAY)
# print(Inew.shape)
# 2. Chuyển ảnh thành mảng 1 chiều x có 784 phần tử (784=28*28).
arr = np.array([])
for i in IgNew:
    arr = np.append(arr, i)

print('arr : ', len(arr))

# 3. Đọc và hiển thị ảnh từ mảng 1 chiều trên
Iarr = arr.reshape((28, 28))
cv2.imshow('Iarr', Iarr.astype(np.uint8))

# # 4. Đọc và hiển thị ảnh trong file mnist.csv
I_csv1 = pd.read_csv('mnist.csv')
Imnist = I_csv1.iloc[20, : 784]
Imnist = Imnist.to_numpy().reshape((28, 28))
cv2.imshow('Imnist', Imnist.astype(np.uint8))

# # 5. Đọc và hiển thị ảnh trong file fashion.csv
I_csv2 = pd.read_csv('fashion.csv')
Ifashion = I_csv2.iloc[99, : 784]
Ifashion = Ifashion.to_numpy().reshape((28, 28))
cv2.imshow('Ifashion', Ifashion.astype(np.uint8))

cv2.waitKey()
