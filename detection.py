import numpy as np
import cv2
import cPickle as pickle

im = cv2.imread('Gun.jpg')
im[im == 255] = 1
im[im == 0] = 255
im[im == 1] = 0
im1 = im.copy()
im2 = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(im2,127,255,0)
contours1, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours2, hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = [contours1,contours2]
file = open('DumpNew.txt', 'w')
pickle.dump(contours, file)
file.close()
cv2.drawContours(im1, contours1, -1, (255,0,0), 3)
temp = 0
for i in range(0, len(contours2)):
    if i % 2 == 0:
        cnt = contours2[i]
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
        temp = i

cv2.imwrite(str(temp+1)+".png",im1)
cv2.imwrite(str(temp)+'.png', im)
cv2.destroyAllWindows()
