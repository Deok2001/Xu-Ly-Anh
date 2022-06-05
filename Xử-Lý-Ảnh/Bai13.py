import cv2
img = cv2.imread("Image/TEST.jpg")
# 13a. Xác định dải giá trị xám của kênh R của I: a=min(R), b=max(R)
red_channel = img[:,:,2]
a = red_channel.min()
b = red_channel.max()
print("Min va max:",a,b)
# 13b. Biến đổi mức xám của kênh R sao cho a=0, b=255 (tăng dải động lên) chinh lai - biến đổi mức xám - tăng dải động xám 
hr = red_channel.shape[0]
wr = red_channel.shape[1]
for i in range(hr):
    for j in range(wr):
         red_channel[i][j]=(255* int(red_channel[i][j]-a))//(b-a)
cv2.imshow('kenh R  bien doi',red_channel)         
# Hiển thị kênh R được biến đổi.
# 13c. Biến đổi tương tự với kênh G và kênh B.
# green
green_channel = img[:,:,1]
ag = green_channel.min()
bg = green_channel.max()
hg = green_channel.shape[0]
wg = green_channel.shape[1]
for i in range(hg):
    for j in range(wg):
         green_channel[i][j]=(255* int(green_channel[i][j]-ag))//(bg-ag)
cv2.imshow('kenh G bien doi',green_channel) 

# blue
blue_channel = img[:,:,2]
ab = blue_channel.min()
bb = blue_channel.max()
hb = blue_channel.shape[0]
wb = blue_channel.shape[1]
for i in range(hb):
    for j in range(wb):
         blue_channel[i][j]=(255* int(blue_channel[i][j]-ab))//(bb-ab)
cv2.imshow('kenh B bien doi',blue_channel) 
cv2.waitKey(0)
cv2.destroyAllWindows()