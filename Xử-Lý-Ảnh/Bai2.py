import cv2

img = cv2.imread('Image/TEST.jpg')
# cách 1
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cach 1', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cách 2
(row, col) = img.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i, j] = sum(img[i, j]) * 0.33
        
cv2.imshow('Cach 2', img)
cv2.waitKey(0)
cv2.destroyAllWindows()