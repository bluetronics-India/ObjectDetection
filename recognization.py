import cv2
import cPickle as pickle

fileNew = open('DumpNew.txt', 'r')
newCon = pickle.load(fileNew)
fileNew.close()
fileClassified = open("DumpClassified.txt", "r")
ClassCon = pickle.load(fileClassified)
fileClassified.close();
sum1 = 0
sum2 = 0
avg1 = 0
avg2 = 0
for i in ClassCon:
    for j in range(len(i[0])):
        for k in range(len(newCon[0])):
            sum1+= cv2.matchShapes(newCon[0][k],i[0][j],cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
        sum1/=k
    sum1/j
    for j in range(len(i[1])):
        for k in range(len(newCon[1])):
            sum2+= cv2.matchShapes(newCon[1][k],i[1][j],cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
        sum2/=k
    sum2/j
avg1 = sum1/10
avg2 = sum2/10
if avg1 <= 0.08 and avg2 <= 0.08:
    print("Its a Match")
else:
    print("Its not a Match")


