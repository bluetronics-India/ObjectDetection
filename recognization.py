import cv2
import cPickle as pickle

fileNew = open('DumpNew.txt', 'r')
newCon = pickle.load(fileNew)
fileNew.close()
fileClassified = open("DumpClassified.txt", "r")
ClassCon = pickle.load(fileClassified)
fileClassified.close()
fileUnClassified = open("DumpUnClassified.txt", "r")
UnClassCon = pickle.load(fileUnClassified)
fileUnClassified.close()

sum1 = 0
sum2 = 0
avg1 = 0
avg2 = 0
sumUn1 = 0
sumUn2 = 0
avgUn1 = 0
avgUn2 = 0

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

for i in UnClassCon:
    for j in range(len(i[0])):
        for k in range(len(newCon[0])):
            sumUn1+= cv2.matchShapes(newCon[0][k],i[0][j],cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
        sumUn1/=k
    sumUn1/j
    for j in range(len(i[1])):
        for k in range(len(newCon[1])):
            sumUn2+= cv2.matchShapes(newCon[1][k],i[1][j],cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
        sumUn2/=k
    sumUn2/j
avgUn1 = sumUn1/10
avgUn2 = sumUn2/10


if avg1 <= avgUn1 or avg2 <= avgUn2:
    print("Its a Match")
else:
    print("Its not a Match")


