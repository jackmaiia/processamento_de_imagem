import cv2
import numpy
from matplotlib import pyplot as plt


def getHist(image):

	#lê a imagem
	img = cv2.imread(image,-1)

	#transforma imagem em tons de cinza
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#aplica blur
	suave = cv2.blur(gray, (7, 7))

	#aplica binarizacao
	ret, bin_img = cv2.threshold(suave, 130,34, cv2.THRESH_BINARY)

	#calcula o histograma da imagem em tons de cinza
	hist_img = cv2.calcHist([bin_img],[0],None,[256],[0,256])
	
	#retorna o histograma pela função
	return hist_img



#percorre todas as imagens
for i in range(1,5):
	for j in range(1,5):
		
		if (i != j) :

			#cria o histograma da imagem 1
			hist_img1 = getHist(f"img/gato00{i}.jpg")

			#cria o histograma da imagem 2
			hist_img2 = getHist(f"img/gato00{j}.jpg")
		
			#faz uma comparação da imagem 1 com a 2 utilizando o metodo cv2.HISTCMP_BHATTACHARYYA
			comp = cv2.compareHist(hist_img1,hist_img2,cv2.HISTCMP_BHATTACHARYYA)

			#exibe em texto qual as imagens que foram comparadas e o resultado da comparação
			print(f"a diferença da imagem gato00{i} com a imagem gato00{j} é: {comp}")

