import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('fotoolhos.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



cv2.imshow('img',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()