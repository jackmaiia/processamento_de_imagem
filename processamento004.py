import cv2
import numpy as np
from random import randint

img = cv2.imread("original.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for i in range(gray.shape[0]):
	for j in range(gray.shape[1]):
			gray[i][j] = randint(0,255)

cv2.imshow("Processada",gray)
cv2.waitKey()
cv2.destroyAllWindows()