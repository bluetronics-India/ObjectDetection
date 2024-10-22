import numpy as np
import cv2
import cPickle as pickle
import urllib2

im = []
contours = []
for i in range(1,10):
    im.append(cv2.imread('classifiedlabled/'+str(i)+'.jpg'))
    im[-1][im == 255] = 1
    im[-1][im == 0] = 255
    im[-1][im == 1] = 0
    im1 = cv2.cvtColor(im[-1],cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(im1, 127, 255,0)
    contours1,hierarchy1 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours2,hierarchy2 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cont = [contours1,contours2]
    contours.append(cont)
    cont = None
file = open('DumpClassified.txt', 'w')
pickle.dump(contours, file)
file.close()

