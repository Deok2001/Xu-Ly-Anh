import cv2
#1 Hiển thị  ảnh I
I = cv2.imread('Image/I04.jpg')
cv2.imshow('Anh goc',I)
#2 Chỉnh size mới cho ảnh là độ cao 256, ảnh giữ nguyên tỷ lệ so với ảnh gốc, được ảnh mới I2. Hiển thị ảnh I2.
(h, w, c) = I.shape
h1=256
w1= h1*w//h
I2 = cv2.resize(I,(h1,w1))
cv2.imshow("Anh Resize", I2)
#3 Chuyển đổi ảnh I sang ảnh HSV được ma trận ảnh Ihsv. Hiển thị kênh V của ảnh Ihsv.
Ihsv=cv2.cvtColor(I,cv2.COLOR_BGR2HSV)
cv2.imshow('Kenh V', Ihsv[:,:,2])
#4 Làm trơn ảnh I trên từng kênh theo phương pháp Gaussain. Hiển thị ảnh I
img = cv2.GaussianBlur(I, (3, 3), 0)
cv2.imshow("Gaussian", img)
#5 Cân bằng histogram của  kênh V của ảnh Ihsv. Hiển thị ảnh Ihsv, so sánh với câu 3. Biến đổi ngược
# ảnh Ihsv về biểu diễn mầu RGB được ảnh I4. Hiển thị ảnh I4.
img_new=img.copy()
img_new[:,:,2]= cv2.equalizeHist(Ihsv[:,:,2])
cv2.imshow('Can bang kenh V',img_new)
I4 = cv2.cvtColor(Ihsv, cv2.COLOR_HSV2BGR)
cv2.imshow("Anh mau RGB", I4)
cv2.waitKey(0) 