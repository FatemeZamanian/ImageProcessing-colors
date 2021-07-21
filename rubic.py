import cv2

org=cv2.imread('index.jpeg')

row,col,ch=org.shape
# bgr
for i in range(row):
    for j in range(col):
        if org[i,j][0]>90 and org[i,j][1]>90 and org[i,j][2]<100:
            org[i,j]=[0,0,255]
        if org[i,j][0]>50 and org[i,j][1]<50 and org[i,j][2]>150:
            org[i, j] = [0, 255, 0]
        if org[i,j][0]<100 and org[i,j][1]>110 and org[i,j][2]>110:
            org[i, j] = [255, 0, 0]

cv2.imshow('',org)
cv2.waitKey()