import cv2 as cv
import numpy as np 

#carrega a imagem em uma varivel
image = cv.imread("9.png")

#cria uma imagem nova em escala de cinza utilizando como padrão
#a imagem carregada anteriormente
#image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
print(type(image))

for y in image:
	if y[3]:
		print(y[3])



#exibe a imagem e coloca o titulo como 'imagem'
#cv.imshow('Imagem',image)

#espera apartar alguma tecla
#cv.waitKey(0)

#destroi todas as janelas
#cv.destroyAllWindows()